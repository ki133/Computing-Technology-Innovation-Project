import React, { useState } from 'react';
import styles from './App.module.css';

function App() {
  const [selectedSection, setSelectedSection] = useState('home');

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
          </div>
        );
      case 'contact':
        return (
          <div>
            <h2>Contact Us</h2>
            <p>If you have any questions or need support, feel free to reach out to us:</p>
            <ul>
              <li>Email: test@student.swin.edu.au</li>
              <li>Phone: 000</li>
              <li>Address: John St, Hawthorn VIC 3122</li>
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
        <h1>Flight Predictor</h1>
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
        <p>&copy;Lucky Eight. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
