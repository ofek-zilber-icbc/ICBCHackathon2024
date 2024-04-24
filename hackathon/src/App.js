
import logo from './logo.svg';
import './App.css';
import ApiCallTest from './apicall_test';
import ListPage from './pages/ListPage';
import DetailsPage from './pages/DetailsPage';

function App() {
  return (
    <div className="App">
      <ListPage/>
      <ApiCallTest/>
      <DetailsPage/>
    </div>
  );
}

export default App;
