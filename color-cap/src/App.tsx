import WebCamComponent from './WebCamComponent';
import "@fontsource/lato";
function App() {

  const appTitle = 'Color Cap';

  return (
    <div style={{height: "100%"}}>
      <header className='header-container'>
        <img alt="App logo" src={require("./images/app-icon.png")} height={50} width={50} />
        {appTitle.toUpperCase()}
      </header>
      <WebCamComponent />
    </div>
  );
}

export default App;
