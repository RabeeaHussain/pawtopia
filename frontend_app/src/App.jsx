import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        {/* <Route path="/virtual" element={<div className="flex items-center justify-center h-screen text-2xl">Virtual Pets - Coming Soon</div>} />
        <Route path="/adopt" element={<div className="flex items-center justify-center h-screen text-2xl">Adopt a Pet - Coming Soon</div>} />
        <Route path="/shop" element={<div className="flex items-center justify-center h-screen text-2xl">Shop - Coming Soon</div>} />
        <Route path="/login" element={<div className="flex items-center justify-center h-screen text-2xl">Login - Coming Soon</div>} /> */}
      </Routes>
    </Router>
  );
}

export default App;
