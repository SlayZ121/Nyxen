import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import StoryLoader from "./components/StoryLoader.jsx";

function App() {
  return (
    <Router>
      <div className="app-container">
        <main>
          <Routes>
            <Route path={"/story/:id"} element={<StoryLoader />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
