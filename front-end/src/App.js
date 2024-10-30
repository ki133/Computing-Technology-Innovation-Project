import React, { useState } from 'react';
import styles from './App.module.css';
import logo from './assets/logo.png';

function App() {
  const [selectedSection, setSelectedSection] = useState('home');
  const [selectedServiceTab, setSelectedServiceTab] = useState('flightPrice');

  const handleLogoClick = () => {
    setSelectedSection('home'); // Navigate to Home when the logo is clicked
  };

  const renderContent = () => {
    switch (selectedSection) {
      case 'home':
        return (
          <div>
            <h2>Welcome to Our Flight Prediction Platform</h2>
            <p>
              Unlock the best deals and never miss a flight update again! Our platform
              predicts flight prices and delays to make your travel planning easier
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
                className={`${styles.tabButton} ${selectedServiceTab === 'flightPrice' ? styles.active : ''}`}
                onClick={() => setSelectedServiceTab('flightPrice')}
              >
                Flight Price
              </button>
              <button
                className={`${styles.tabButton} ${selectedServiceTab === 'flightSchedule' ? styles.active : ''}`}
                onClick={() => setSelectedServiceTab('flightSchedule')}
              >
                Flight Schedule
              </button>
            </div>
            <div className={styles.tabContent}>
              {selectedServiceTab === 'flightPrice' ? (
                <div>
                  <h3>Flight Price Prediction</h3>
                  <p>Get insights into the best times to book flights at the lowest prices.</p>
                </div>
              ) : (
                <div>
                  <h3>Flight Schedule and Delays</h3>
                  <p>Stay updated on flight schedules and potential delays for better planning.</p>
                </div>
              )}
            </div>
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
        <img src={logo} alt="Lucky Flight Logo" className={styles.logo} onClick={handleLogoClick} /> {/* Logo is clickable */}
        <h1 className={styles.title}>Flight Prediction Platform</h1>
      </header>
      <div className={styles.body}>
        <aside className={styles.sidebar}>
          <nav>
            <ul>
              <li>
                <button onClick={() => setSelectedSection('home')}>Home</button>
              </li>
              <li>
                <button onClick={() => setSelectedSection('about')}>About</button>
              </li>
              <li>
                <button onClick={() => setSelectedSection('services')}>Services</button>
              </li>
              <li>
                <button onClick={() => setSelectedSection('contact')}>Contact</button>
              </li>
            </ul>
          </nav>
        </aside>
        <main className={styles.mainContent}>
          {renderContent()}
        </main>
      </div>
      <footer className={styles.footer}>
        <p>&copy; Lucky Eight. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
