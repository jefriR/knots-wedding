import React, { useState } from "react";
import App from "./App";
import AppWhite from "./AppWhite";
import "./index.css";
import "./index-white.css";

function Comparison() {
  const [activeVersion, setActiveVersion] = useState("white");

  return (
    <div>
      {/* Version Selector */}
      <div style={{
        position: 'fixed',
        top: '20px',
        right: '20px',
        zIndex: 9999,
        background: 'white',
        padding: '12px 20px',
        borderRadius: '0px',
        border: '2px solid #000',
        boxShadow: '0 4px 12px rgba(0,0,0,0.15)',
        display: 'flex',
        gap: '12px',
        alignItems: 'center'
      }}>
        <span style={{ fontSize: '12px', fontWeight: '600', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
          Color Scheme:
        </span>
        <button
          onClick={() => setActiveVersion("beige")}
          style={{
            padding: '8px 16px',
            background: activeVersion === "beige" ? '#fffef2' : 'white',
            border: activeVersion === "beige" ? '2px solid #333' : '1px solid #ccc',
            borderRadius: '0px',
            cursor: 'pointer',
            fontSize: '12px',
            fontWeight: activeVersion === "beige" ? '600' : '400',
            textTransform: 'uppercase',
            letterSpacing: '0.05em',
            transition: 'all 0.2s ease'
          }}
        >
          Warm Beige
        </button>
        <button
          onClick={() => setActiveVersion("white")}
          style={{
            padding: '8px 16px',
            background: activeVersion === "white" ? '#d4af37' : 'white',
            color: activeVersion === "white" ? '#000' : '#333',
            border: activeVersion === "white" ? '2px solid #d4af37' : '1px solid #ccc',
            borderRadius: '0px',
            cursor: 'pointer',
            fontSize: '12px',
            fontWeight: activeVersion === "white" ? '600' : '400',
            textTransform: 'uppercase',
            letterSpacing: '0.05em',
            transition: 'all 0.2s ease'
          }}
        >
          White/Gold
        </button>
      </div>

      {/* Render Selected Version */}
      {activeVersion === "beige" ? <App /> : <AppWhite />}
    </div>
  );
}

export default Comparison;
