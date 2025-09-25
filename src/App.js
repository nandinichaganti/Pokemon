




import pokeball from './pokeball.png';

function App() {
  return (
    <div style={{
      minHeight: '100vh',
      width: '100vw',
      overflow: 'hidden',
      position: 'relative',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
    }}>
      {/* Blurred Pokeball background */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100vw',
          height: '100vh',
          zIndex: 0,
          background: `#222 url(${pokeball}) center center / cover no-repeat`,
          filter: 'blur(18px) brightness(1.1)',
          opacity: 0.8,
        }}
      />
      {/* Foreground content */}
      <div style={{
        position: 'relative',
        zIndex: 1,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        width: '100%',
      }}>
        <h1 style={{
          fontSize: '4rem',
          fontWeight: 'bold',
          color: '#FFD600',
          textShadow: '2px 2px 8px #000',
          margin: 0,
          letterSpacing: '0.1em',
          textAlign: 'center',
        }}>
          Pokemon
        </h1>
        <button
          style={{
            marginTop: 40,
            fontSize: '1.5rem',
            padding: '16px 40px',
            borderRadius: 8,
            border: 'none',
            background: '#FFD600',
            color: '#222',
            fontWeight: 'bold',
            cursor: 'pointer',
            boxShadow: '0 4px 16px rgba(0,0,0,0.2)'
          }}
        >
          create your team
        </button>
      </div>
    </div>
  );
}

export default App;
