from pyexpat import model
import re

import pytest

import numpy
import pandas
import scipy.sparse
from formulaic import Formula, ModelSpec, ModelSpecs, ModelMatrix, ModelMatrices
from formulaic.materializers.base import FormulaMaterializerMeta
from formulaic.materializers.pandas import PandasMaterializer
from formulaic.parser.types import Factor, Term


class TestModelSpec:
    @pytest.fixture
    def data(self):
        return pandas.DataFrame(
            {
                "A": ["a", "b", "c"],
                "a": [0, 0, 1],
            }
        )

    @pytest.fixture
    def data2(self):
        return pandas.DataFrame(
            {
                "A": ["a", "a", "a"],
                "a": [0, 0, 1],
            }
        )

    @pytest.fixture
    def formula(self):
        return Formula("a + A + A:a")

    @pytest.fixture
    def model_spec(self, formula, data):
        return formula.get_model_matrix(data).model_spec

    def test_constructor(self):
        with pytest.raises(
            ValueError,
            match=re.escape(
                r"Nominated `Formula` instance has structure, which is not permitted when attaching to a `ModelSpec` instance."
            ),
        ):
            ModelSpec(formula=Formula("y ~ x"))

    @pytest.mark.filterwarnings(
        r"ignore:`ModelSpec\.feature_.*` is deprecated.*:DeprecationWarning"
    )
    def test_attributes(self, model_spec):
        assert model_spec.formula == Formula("a + A + A:a")
        assert model_spec.ensure_full_rank is True
        assert model_spec.materializer == "pandas"
        assert model_spec.column_names == (
            "Intercept",
            "a",
            "A[T.b]",
            "A[T.c]",
            "A[T.b]:a",
            "A[T.c]:a",
        )
        assert model_spec.column_indices == {
            "Intercept": 0,
            "a": 1,
            "A[T.b]": 2,
            "A[T.c]": 3,
            "A[T.b]:a": 4,
            "A[T.c]:a": 5,
        }
        assert model_spec.term_slices == {
            "1": slice(0, 1),
            "a": slice(1, 2),
            "A": slice(2, 4),
            "A:a": slice(4, 6),
        }
        assert model_spec.terms == ["1", "a", "A", "A:a"]
        assert model_spec.term_variables == {
            "1": set(),
            "a": {"a"},
            "A": {"A"},
            "A:a": {"a", "A"},
        }
        assert model_spec.variable_terms == {"a": {"a", "A:a"}, "A": {"A", "A:a"}}
        assert model_spec.variable_indices == {
            "a": [1, 4, 5],
            "A": [2, 3, 4, 5],
        }
        assert model_spec.variables == {"a", "A"}
        assert model_spec.variables_by_source == {"data": {"a", "A"}}

    def test_get_model_matrix(self, model_spec, data2):
        m = model_spec.get_model_matrix(data2)

        assert isinstance(m, pandas.DataFrame)
        assert model_spec.column_names == tuple(m.columns)

        model_spec = model_spec.update(materializer=None)
        m2 = model_spec.get_model_matrix(data2)
        assert isinstance(m2, pandas.DataFrame)
        assert model_spec.column_names == tuple(m2.columns)

        m3 = model_spec.get_model_matrix(data2, output="sparse")
        assert isinstance(m3, scipy.sparse.spmatrix)

    def test_get_linear_constraints(self, model_spec):
        lc = model_spec.get_linear_constraints("`A[T.b]` - a = 3")
        assert numpy.allclose(lc.constraint_matrix, [[0.0, -1.0, 1.0, 0, 0.0, 0.0]])
        assert lc.constraint_values == [3]
        assert lc.variable_names == model_spec.column_names

    def test_differentiate(self, model_spec, formula):
        assert model_spec.differentiate("a").formula == formula.differentiate("a")

    def test_get_slice(self, model_spec):
        s = slice(0, 1)
        assert model_spec.get_slice(s) is s
        assert model_spec.get_slice(0) == s
        assert model_spec.get_slice(model_spec.terms[1]) == slice(1, 2)
        assert model_spec.get_slice("A") == slice(2, 4)
        assert model_spec.get_slice("A[T.b]") == slice(2, 3)

        with pytest.raises(
            ValueError,
            match=re.escape(
                r"Model matrices built using this spec do not include term: `missing`."
            ),
        ):
            model_spec.get_slice(Term(factors=[Factor("missing")]))

        with pytest.raises(
            ValueError,
            match=re.escape(
                r"Model matrices built using this spec do not have any columns related to: `'missing'`."
            ),
        ):
            model_spec.get_slice("missing")

    def test_model_specs(self, model_spec, data2):
        model_specs = ModelSpecs(a=model_spec)

        assert isinstance(model_specs.get_model_matrix(data2), ModelMatrices)
        assert isinstance(model_specs.get_model_matrix(data2).a, ModelMatrix)
        assert numpy.all(
            model_specs.get_model_matrix(data2).a == model_spec.get_model_matrix(data2)
        )
        sparse_matrices = model_specs.get_model_matrix(data2, output="sparse")
        assert isinstance(sparse_matrices, ModelMatrices)
        assert isinstance(sparse_matrices.a, scipy.sparse.spmatrix)

        # Validate missing materializer and output type behaviour
        model_specs2 = ModelSpecs(
            lhs=ModelSpec(formula="A"), rhs=ModelSpec(formula="a")
        )
        assert numpy.all(
            model_specs2.get_model_matrix(data2).lhs
            == ModelSpec(formula="A").get_model_matrix(data2)
        )

        # Validate non-joint generation of model matrices
        class MyPandasMaterializer(PandasMaterializer):
            REGISTER_NAME = "my_pandas_materializer"

        incompatible_specs = ModelSpecs(
            a=model_spec, b=model_spec.update(materializer=MyPandasMaterializer)
        )
        matrices = incompatible_specs.get_model_matrix(data2)
        assert isinstance(matrices, ModelMatrices)
        assert numpy.all(matrices.a == model_spec.get_model_matrix(data2))
        assert numpy.all(matrices.b == model_spec.get_model_matrix(data2))

        FormulaMaterializerMeta.REGISTERED_NAMES.pop("my_pandas_materializer")

        # Validate differentiation
        assert model_specs.differentiate("a").a == model_spec.differentiate("a")

        # Validate invalid type checking
        with pytest.raises(TypeError, match="`ModelSpecs` instances expect all.*"):
            ModelSpecs("invalid type!")

    def test_empty(self):
        model_spec = ModelSpec([])

        with pytest.raises(
            RuntimeError,
            match=re.escape(
                "`ModelSpec.structure` has not yet been populated. This will "
                "likely be resolved by using the `ModelSpec` instance attached "
                "to the model matrix generated when calling `.get_model_matrix()`."
            ),
        ):
            model_spec.column_names

        with pytest.raises(
            RuntimeError,
            match=re.escape(
                "`ModelSpec.structure` has not yet been populated. This will "
                "likely be resolved by using the `ModelSpec` instance attached "
                "to the model matrix generated when calling `.get_model_matrix()`."
            ),
        ):
            model_spec.term_indices

        with pytest.raises(
            RuntimeError,
            match=re.escape(
                "`ModelSpec.structure` has not yet been populated. This will "
                "likely be resolved by using the `ModelSpec` instance attached "
                "to the model matrix generated when calling `.get_model_matrix()`."
            ),
        ):
            model_spec.term_variables

    def test_unrepresented_term(self):
        model_spec = (
            Formula("A")
            .get_model_matrix(pandas.DataFrame({"A": ["a", "a", "a"]}))
            .model_spec
        )

        assert model_spec.term_indices == {
            "1": [0],
            "A": [],
        }
        assert model_spec.term_slices == {
            "1": slice(0, 1),
            "A": slice(0, 0),
        }
