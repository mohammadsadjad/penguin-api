from locust import HttpUser, task, between

class PenguinPredictUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def predict_species(self):
        self.client.post("/predict", json={
            "bill_length_mm": 39.5,
            "bill_depth_mm": 17.4,
            "flipper_length_mm": 186.0,
            "body_mass_g": 3800.0
        })
