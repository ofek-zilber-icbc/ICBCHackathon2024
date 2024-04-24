
import logo from './logo.svg';
import './App.css';
import ApiCallTest from './apicall_test';
import ListPage from './pages/ListPage';
import DetailsPage from './pages/DetailsPage';
import { Routes, Route , Router, BrowserRouter } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<ListPage/>}/>
        <Route path='/details' element={<DetailsPage/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;