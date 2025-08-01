from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_valid_input():
    """Test prediction with valid penguin data"""
    sample_data = {
        "bill_length_mm": 39.1,
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": 3750
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 200
    assert "prediction" in response.json()


def test_predict_missing_field():
    """Test request with missing field"""
    sample_data = {
        "bill_length_mm": 39.1,
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181
        # missing body_mass_g
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 422  # Unprocessable Entity


def test_predict_invalid_type():
    """Test request with string instead of float"""
    sample_data = {
        "bill_length_mm": "hello",
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": 3750
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 422


def test_predict_negative_values():
    """Test request with out-of-range values"""
    sample_data = {
        "bill_length_mm": -1,
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": 3750
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 422
