// src/App.js

import React, { useState } from 'react';
import styles from './App.module.css';
import logo from './assets/logo.png';
import DelayForm from './components/DelayForm';
import PriceForm from './components/PriceForm';
import TravelForm from './components/TravelForm';

function App() {
  const [selectedSection, setSelectedSection] = useState('home');
  const [selectedServiceTab, setSelectedServiceTab] = useState('flightSchedule'); // Default to Delay Prediction
  const [result, setResult] = useState(null); // Store prediction results here

  const handleLogoClick = () => {
    setSelectedSection('home');
    setResult(null); // Clear results when navigating to home
  };

  const renderContent = () => {
    switch (selectedSection) {
      case 'home':
        return (
          <div>
            <h2>Welcome to Our Flight Prediction Platform</h2>
            <p>
              Unlock the best deals and never miss a flight update again! Our platform
              predicts flight prices, delays, and travel metrics to make your travel planning easier
              and smarter.
            </p>
          </div>
        );
      case 'about':
        return (
          <div>
            <h2>About Us</h2>
            <p>
              We are a team of travel enthusiasts and data experts, passionate about
              making travel more accessible and hassle-free. Our prediction algorithms
              help you find the best flight deals and avoid unexpected delays.
            </p>
          </div>
        );
      case 'services':
        return (
          <div>
            <h2>Our Services</h2>
            <div className={styles.tabContainer}>
              <button
                className={`${styles.tabButton} ${selectedServiceTab === 'flightSchedule' ? styles.active : ''}`}
                onClick={() => { setSelectedServiceTab('flightSchedule'); setResult(null); }}
              >
                Flight Delay Prediction
              </button>
              <button
                className={`${styles.tabButton} ${selectedServiceTab === 'flightPrice' ? styles.active : ''}`}
                onClick={() => { setSelectedServiceTab('flightPrice'); setResult(null); }}
              >
                Flight Price Prediction
              </button>
              <button
                className={`${styles.tabButton} ${selectedServiceTab === 'travelMetrics' ? styles.active : ''}`}
                onClick={() => { setSelectedServiceTab('travelMetrics'); setResult(null); }}
              >
                Travel Metrics Prediction
              </button>
            </div>
            <div className={styles.tabContent}>
              {selectedServiceTab === 'flightSchedule' && <DelayForm setResult={setResult} />}
              {selectedServiceTab === 'flightPrice' && <PriceForm setResult={setResult} />}
              {selectedServiceTab === 'travelMetrics' && <TravelForm setResult={setResult} />}
            </div>
            {result && (
              <div className={styles.result}>
                <h3>Prediction Result:</h3>
                <pre>{JSON.stringify(result, null, 2)}</pre>
              </div>
            )}
          </div>
        );
      case 'contact':
        return (
          <div>
            <h2>Contact Us</h2>
            <p>If you have any questions or need support, feel free to reach out to us:</p>
            <ul>
              <li>Email: support@flightpredict.com</li>
              <li>Phone: +1 (123) 456-7890</li>
              <li>Address: 123 Travel Street, Journey City, USA</li>
            </ul>
          </div>
        );
      default:
        return null;
    }
  };

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <img src={logo} alt="Lucky Flight Logo" className={styles.logo} onClick={handleLogoClick} />
        <h1 className={styles.title}>Flight Prediction Platform</h1>
      </header>
      <div className={styles.body}>
        <aside className={styles.sidebar}>
          <nav>
            <ul>
              <li>
                <button onClick={() => { setSelectedSection('home'); setResult(null); }}>Home</button>
              </li>
              <li>
                <button onClick={() => { setSelectedSection('about'); setResult(null); }}>About</button>
              </li>
              <li>
                <button onClick={() => { setSelectedSection('services'); setResult(null); }}>Services</button>
              </li>
              <li>
                <button onClick={() => { setSelectedSection('contact'); setResult(null); }}>Contact</button>
              </li>
            </ul>
          </nav>
        </aside>
        <main className={styles.mainContent}>
          {renderContent()}
        </main>
      </div>
      <footer className={styles.footer}>
        <p>&copy; 2024 Flight Prediction Platform. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
