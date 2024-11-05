import React, { useState } from 'react';
import axios from 'axios';

function DelayForm() {
  const [formData, setFormData] = useState({
    airline: '',
    departingPort: '',
    arrivingPort: '',
    month: 1,
    year: 2023,
  });
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  // Update form data as user inputs values
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null); // Reset error state

    try {
      // Send POST request to FastAPI backend
      const response = await axios.post('http://127.0.0.1:8000/api/delay/predict', {
        airline: formData.airline,
        departing_port: formData.departingPort,
        arriving_port: formData.arrivingPort,
        month: parseInt(formData.month, 10),
        year: parseInt(formData.year, 10),
      });

      // Update result state with prediction response
      setResult(response.data);
    } catch (error) {
      setError('Failed to fetch prediction. Please try again.');
    }
  };

  return (
    <div>
      <h2>Delay Prediction</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Airline:
          <input
            type="text"
            name="airline"
            value={formData.airline}
            onChange={handleChange}
            placeholder="Enter airline name"
            required
          />
        </label>
        <label>
          Departing Port:
          <input
            type="text"
            name="departingPort"
            value={formData.departingPort}
            onChange={handleChange}
            placeholder="Enter departing port"
            required
          />
        </label>
        <label>
          Arriving Port:
          <input
            type="text"
            name="arrivingPort"
            value={formData.arrivingPort}
            onChange={handleChange}
            placeholder="Enter arriving port"
            required
          />
        </label>
        <label>
          Month:
          <input
            type="number"
            name="month"
            value={formData.month}
            onChange={handleChange}
            min="1"
            max="12"
            required
          />
        </label>
        <label>
          Year:
          <input
            type="number"
            name="year"
            value={formData.year}
            onChange={handleChange}
            min="2023"
            required
          />
        </label>
        <button type="submit">Predict Delay</button>
      </form>

      {result && (
        <div>
          <h3>Prediction Result:</h3>
          <p>Is Delayed: {result.is_delayed ? 'Yes' : 'No'}</p>
          <p>Probability of Delay: {result.probability_of_delay.toFixed(2)}</p>
        </div>
      )}

      {error && (
        <div style={{ color: 'red' }}>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
}

export default DelayForm;
