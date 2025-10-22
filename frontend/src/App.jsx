// import React from "react";
// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// // Pages
// import Home from "./pages/Home";
// import Pets from "./pages/Pets";
// import Login from "./pages/Login";
// import Signup from "./pages/Signup";
// import AdoptPets from "./pages/AdoptPets";
// import PetProducts from "./pages/PetProducts";

// // Components
// import Navbar from "./components/Navbar";

// export default function App() {
//   return (
//     <Router>
//       {/* Navbar at the top */}
//       <Navbar />

//       {/* Main Content Area (with top padding so content isn’t hidden under navbar) */}
//       {/* <div className="pt-20">        <Routes>
//           <Route path="/" element={<Home />} />
//           <Route path="/virtual" element={<Pets />} />
//           <Route path="/pets" element={<Pets />} /> 
//           <Route path="/adopt" element={<AdoptPets />} />
//           <Route path="/shop" element={<PetProducts />} />
//           <Route path="/login" element={<Login />} />
//           <Route path="/signup" element={<Signup />} />
//         </Routes>
//       </div>  */}
//     </Router>
//   );
// }

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/virtual" element={<div className="flex items-center justify-center h-screen text-2xl">Virtual Pets - Coming Soon</div>} />
        <Route path="/adopt" element={<div className="flex items-center justify-center h-screen text-2xl">Adopt a Pet - Coming Soon</div>} />
        <Route path="/shop" element={<div className="flex items-center justify-center h-screen text-2xl">Shop - Coming Soon</div>} />
        <Route path="/login" element={<div className="flex items-center justify-center h-screen text-2xl">Login - Coming Soon</div>} />
      </Routes>
    </Router>
  );
}

export default App;

