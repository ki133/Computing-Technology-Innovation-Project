const BASE_URL = "http://127.0.0.1:8000/api";

export const fetchPricePrediction = async (inputData) => {
  const response = await fetch(`${BASE_URL}/price/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(inputData),
  });
  const data = await response.json();
  return data;
};

export const fetchDelayPrediction = async (inputData) => {
  const response = await fetch(`${BASE_URL}/delay/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(inputData),
  });
  const data = await response.json();
  return data;
};

export const fetchTravelPrediction = async (inputData) => {
  const response = await fetch(`${BASE_URL}/travel/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(inputData),
  });
  const data = await response.json();
  return data;
};
