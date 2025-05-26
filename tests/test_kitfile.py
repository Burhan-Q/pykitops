from pathlib import Path

import pytest

from kitops.modelkit.kitfile import Kitfile


class TestKitfileCreation:
    def test_create_full_kitfile(self, fixtures: dict[str, Path]):
        """Test creation of a full Kitfile from a fixture."""
        kitfile_path = fixtures["Kitfile_full"]
        kitfile = Kitfile(path=str(kitfile_path))
        assert kitfile is not None
        assert kitfile.manifestVersion == "1.0"
        assert kitfile is not None and kitfile.package.name == "Titanic-Survivability-Predictor"
        assert kitfile is not None and kitfile.model.name == "titanic-survivability-predictor"

    def test_create_blank_kitfile(self):
        """Test creation of a blank Kitfile."""
        kitfile = Kitfile()
        assert kitfile is not None and kitfile == Kitfile()

    def test_create_from_template(self, fixtures: dict[str, Path]):
        """Test creation of a Kitfile from a template."""
        kitfile_path = fixtures["Kitfile_full"]
        with pytest.raises(ValueError):
            kitfile = Kitfile(path=str(kitfile_path), manifestVersion="6.9.0")
            assert kitfile is not None and kitfile.manifestVersion == "6.9.0"  # this won't run

    def test_create_from_kwargs(self):
        """Test creation of a Kitfile from keyword arguments."""
        kitfile = Kitfile(
            manifestVersion="6.6.6",
            package={
                "name": "Package Packer",
                "version": "5.2.5",
                "description": "Package your packages with Package Packer",
                "authors": ["Patrick Packer"],
            },
            model={
                "name": "Pack Model",
                "path": "pack_model_path/",
                "framework": "PackageRT",
                "version": "1.2.3",
                "description": "Model for packing packages",
                "license": "Pack License",
                "parts": [],
                "parameters": "",
            },
        )
        assert kitfile.manifestVersion == "6.6.6"
        assert kitfile.package.name == "Package Packer"
        assert kitfile.model.name == "Pack Model"


class TestKitfileMutation:
    def full_kitfile(self, fixtures: dict[str, Path]) -> Kitfile:
        kitfile_path = fixtures["Kitfile_full"]
        return Kitfile(path=str(kitfile_path))

    def test_mutate_manifestVersion(self, fixtures: dict[str, Path]):
        """Test mutation of manifestVersion attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)

        kitfile.manifestVersion = "2.0"
        assert kitfile.manifestVersion == "2.0"
        with pytest.raises(TypeError):
            kitfile.manifestVersion = []  # type: ignore

    def test_mutate_package(self, fixtures: dict[str, Path]):
        """Test mutation of package attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)
        kitfile.package = {
            "name": "New Package Name",
            "version": "2.0.0",
            "description": "Updated description",
            "authors": ["New Author"],
        }
        kitfile.package.name = "Newer Package Name"
        assert kitfile.package.name == "Newer Package Name"
        with pytest.raises(TypeError):
            kitfile.package = 123  # type: ignore

    def test_mutate_model(self, fixtures: dict[str, Path]):
        """Test mutation of model attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)
        kitfile.model = {
            "name": "New Model Name",
            "path": "new_model_path/",
            "framework": "new_framework",
            "version": "2.0.0",
            "description": "Updated model description",
            "license": "New License",
            "parts": [],
            "parameters": "",
        }
        kitfile.model.name = "Newer Model Name"
        assert kitfile.model.name == "Newer Model Name"
        with pytest.raises(TypeError):
            kitfile.model = 123  # type: ignore

    def test_mutate_code(self, fixtures: dict[str, Path]):
        """Test mutation of code attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)
        kitfile.code = [
            {
                "path": "new_code_path/",
                "description": "Updated code description",
                "license": "New Code License",
            }
        ]
        kitfile.code[0].path = "new_code_path2/"
        assert kitfile.code[0].path == "new_code_path2/"
        with pytest.raises(TypeError):
            kitfile.code = 123  # type: ignore

    def test_mutate_datasets(self, fixtures: dict[str, Path]):
        """Test mutation of datasets attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)
        kitfile.datasets = [
            {
                "name": "New Dataset Name",
                "path": "new_dataset_path/",
                "description": "Updated dataset description",
                "license": "New Dataset License",
            }
        ]
        kitfile.datasets[0].name = "Newer Dataset Name"
        assert kitfile.datasets[0].name == "Newer Dataset Name"
        with pytest.raises(TypeError):
            kitfile.datasets = 123  # type: ignore

    def test_mutate_docs(self, fixtures: dict[str, Path]):
        """Test mutation of docs attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)
        kitfile.docs = [
            {
                "path": "new_docs_path/",
                "description": "Updated docs description",
            }
        ]
        kitfile.docs[0].path = "new_docs_path2/"
        assert kitfile.docs[0].path == "new_docs_path2/"
        with pytest.raises(TypeError):
            kitfile.docs = 123  # type: ignore


class TestKitfileAttributeAccess:
    def full_kitfile(self, fixtures: dict[str, Path]) -> Kitfile:
        kitfile_path = fixtures["Kitfile_full"]
        return Kitfile(path=str(kitfile_path))

    def test_access_manifestVersion(self, fixtures: dict[str, Path]):
        """Test access to manifestVersion attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)
        assert kitfile.manifestVersion == "1.0"

    def test_access_package(self, fixtures: dict[str, Path]):
        """Test access to package attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)

        assert kitfile.package.name == "Titanic-Survivability-Predictor"
        assert kitfile.package["name"] == "Titanic-Survivability-Predictor"
        assert kitfile.package.get("name") == "Titanic-Survivability-Predictor"

        assert kitfile.package.version == "1.0.0"
        assert kitfile.package["version"] == "1.0.0"
        assert kitfile.package.get("version") == "1.0.0"

        assert (
            kitfile.package.description
            == "A model attempting to predict passenger survivability of  the Titanic Shipwreck"
        )
        assert (
            kitfile.package["description"]
            == "A model attempting to predict passenger survivability of  the Titanic Shipwreck"
        )
        assert (
            kitfile.package.get("description")
            == "A model attempting to predict passenger survivability of  the Titanic Shipwreck"
        )

        assert kitfile.package.authors == ["Jozu"]
        assert kitfile.package["authors"] == ["Jozu"]
        assert kitfile.package.get("authors") == ["Jozu"]

    def test_access_model(self, fixtures: dict[str, Path]):
        """Test access to model attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)

        assert kitfile.model.name == "titanic-survivability-predictor"
        assert kitfile.model["name"] == "titanic-survivability-predictor"
        assert kitfile.model.get("name") == "titanic-survivability-predictor"

        assert kitfile.model.path == "model"
        assert kitfile.model["path"] == "model"
        assert kitfile.model.get("path") == "model"

        assert kitfile.model.framework == "joblib"
        assert kitfile.model["framework"] == "joblib"
        assert kitfile.model.get("framework") == "joblib"

        assert kitfile.model.version == "1.0"
        assert kitfile.model["version"] == "1.0"
        assert kitfile.model.get("version") == "1.0"

        assert kitfile.model.description == "Directory containing figures and graphs exported as image files."
        assert kitfile.model["description"] == "Directory containing figures and graphs exported as image files."
        assert kitfile.model.get("description") == "Directory containing figures and graphs exported as image files."

        assert kitfile.model.license == "Apache-2.0"
        assert kitfile.model["license"] == "Apache-2.0"
        assert kitfile.model.get("license") == "Apache-2.0"

    def test_access_code(self, fixtures: dict[str, Path]):
        """Test access to code attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)
        expected: list[dict[str, str]] = [
            {
                "path": "requirements.txt",
                "description": "Python packages required by this example.",
                "license": "Apache-2.0",
            },
            {
                "path": "titanic_survivability.ipynb",
                "description": "Jupyter Notebook used to train, validate, optimize and  export the model.",
                "license": "Apache-2.0",
            },
        ]

        for c, e in zip(kitfile.code, expected):
            assert c.path == e["path"]
            assert c["path"] == e["path"]
            assert c.get("path") == e["path"]

            assert c.description == e["description"]
            assert c["description"] == e["description"]
            assert c.get("description") == e["description"]

            assert c.license == e["license"]
            assert c["license"] == e["license"]
            assert c.get("license") == e["license"]

    def test_access_datasets(self, fixtures: dict[str, Path]):
        """Test access to datasets attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)
        expected: list[dict[str, str]] = [
            {
                "name": "training",
                "path": "data/train.csv",
                "description": "Data to be used for model training.",
                "license": "Apache-2.0",
            },
            {
                "name": "testing",
                "path": "data/test.csv",
                "description": "Data to be used for model testing.",
                "license": "Apache-2.0",
            },
        ]

        for d, e in zip(kitfile.datasets, expected):
            assert d.name == e["name"]
            assert d["name"] == e["name"]
            assert d.get("name") == e["name"]

            assert d.path == e["path"]
            assert d["path"] == e["path"]
            assert d.get("path") == e["path"]

            assert d.description == e["description"]
            assert d["description"] == e["description"]
            assert d.get("description") == e["description"]

            assert d.license == e["license"]
            assert d["license"] == e["license"]
            assert d.get("license") == e["license"]
    
    def test_access_docs(self, fixtures: dict[str, Path]):
        """Test access to docs attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)
        expected: list[dict[str, str]] = [
            {
                "path": "README.md",
                "description": "Important notes about the project.",
            },
            {
                "path": "images",
                "description": "Directory containing figures and graphs exported as image files.",
            },
        ]

        for d, e in zip(kitfile.docs, expected):
            assert d.path == e["path"]
            assert d["path"] == e["path"]
            assert d.get("path") == e["path"]

            assert d.description == e["description"]
            assert d["description"] == e["description"]
            assert d.get("description") == e["description"]
    
    def test_access_parts(self, fixtures: dict[str, Path]):
        """Test access to parts attribute in Kitfile."""
        kitfile = self.full_kitfile(fixtures)
        expected_parts = [
            {"path": "config.json", "name": "config", "type": "config file"},
            {"path": "tokenizer.json"},
            {"path": "tokenizer_config.json"},
            {"path": "vocab.txt"},
        ]

        if kitfile.model.parts is not None:
            for part, expected in zip(kitfile.model.parts, expected_parts):
                assert part.path == expected["path"]
                assert part["path"] == expected["path"]
                assert part.get("path") == expected["path"]

                if "name" in expected:
                    assert part.name == expected["name"]
                    assert part["name"] == expected["name"]
                    assert part.get("name") == expected["name"]

                if "type" in expected:
                    assert part.type == expected["type"]
                    assert part["type"] == expected["type"]
                    assert part.get("type") == expected["type"]