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
            manifestVersion="1.0",
            package={
                "name": "Test Package",
                "version": "0.1.0",
                "description": "A test package",
                "authors": ["Test Author"],
            },
            model={
                "name": "Test Model",
                "path": "test_model_path/",
                "framework": "test_framework",
                "version": "1.0.0",
                "description": "A test model",
                "license": "Test License",
                "parts": [],
                "parameters": "",
            },
        )
        assert kitfile.manifestVersion == "1.0"
        assert kitfile.package.name == "Test Package"
        assert kitfile.model.name == "Test Model"


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
