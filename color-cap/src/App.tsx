import WebCamComponent from './WebCamComponent';

function App() {

  const appTitle = 'Color Cap';

  return (
    <div style={{height: "100%"}}>
      <header className='header-container'>
        {appTitle.toUpperCase()}
      </header>
      <WebCamComponent />
    </div>
  );
}

export default App;
