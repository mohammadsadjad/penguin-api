from locust import HttpUser, task, between

class PredictUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def predict_penguin(self):
        payload = {
            "culmen_length_mm": 39.2,
            "culmen_depth_mm": 17.3,
            "flipper_length_mm": 180.0,
            "body_mass_g": 3800.0
        }
        self.client.post("/predict", json=payload)
