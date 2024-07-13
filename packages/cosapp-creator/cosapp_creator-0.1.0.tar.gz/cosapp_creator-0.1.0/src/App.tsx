import './App.css';
import { CoSAppCreator } from './cosappcreatormodule';
function App() {
  const root = document.getElementById('root');
  const baseUrl = root?.dataset?.cosappUrl;
  return <CoSAppCreator baseUrl={baseUrl} />;
}

export default App;
