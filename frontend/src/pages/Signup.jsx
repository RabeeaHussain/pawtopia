import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import MessageBox from "../components/MessageBox";

export default function Signup() {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [messageBox, setMessageBox] = useState(null);
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    setMessageBox(null);
    try {
      const res = await axios.post("http://127.0.0.1:8000/users/register", {
        username,
        email,
        password,
      });

      localStorage.setItem("token", res.data.access_token);
      setMessageBox({ text: "Signup successful! Redirecting...", type: "success" });
      setTimeout(() => navigate("/pets"), 1500);
    } catch (err) {
      console.error("Signup error:", err);
      if (err.response?.data?.detail === "Email already registered") {
        setMessageBox({ text: "This email is already registered.", type: "error" });
      } else {
        setMessageBox({ text: "Signup failed. Please try again.", type: "error" });
      }
    }
  };

  return null;  
  // return (
  //   <div className="flex items-center justify-center min-h-screen bg-amber-50 p-4">
  //     <div className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-sm">
  //       <h2 className="text-2xl font-bold mb-6 text-center text-amber-700">
  //         🐾 Create Your Pawtopia Account
  //       </h2>

  //       <form onSubmit={handleSignup} className="space-y-4">
  //         <input
  //           type="text"
  //           placeholder="Username"
  //           value={username}
  //           onChange={(e) => setUsername(e.target.value)}
  //           className="border border-gray-300 p-3 rounded-lg w-full focus:ring-amber-500 focus:border-amber-500 transition"
  //           required
  //         />
  //         <input
  //           type="email"
  //           placeholder="Email"
  //           value={email}
  //           onChange={(e) => setEmail(e.target.value)}
  //           className="border border-gray-300 p-3 rounded-lg w-full focus:ring-amber-500 focus:border-amber-500 transition"
  //           required
  //         />
  //         <input
  //           type="password"
  //           placeholder="Password"
  //           value={password}
  //           onChange={(e) => setPassword(e.target.value)}
  //           className="border border-gray-300 p-3 rounded-lg w-full focus:ring-amber-500 focus:border-amber-500 transition"
  //           required
  //         />
  //         <button
  //           type="submit"
  //           className="w-full bg-amber-600 text-white py-3 rounded-xl font-semibold hover:bg-amber-700 transition-transform active:scale-95"
  //         >
  //           Sign Up
  //         </button>
  //       </form>

  //       <p className="text-center mt-6 text-sm text-gray-600">
  //         Already have an account?{" "}
  //         <span
  //           onClick={() => navigate("/login")}
  //           className="text-amber-600 hover:underline cursor-pointer font-medium"
  //         >
  //           Log In
  //         </span>
  //       </p>
  //     </div>

  //     {messageBox && (
  //       <MessageBox
  //         message={messageBox.text}
  //         type={messageBox.type}
  //         onClose={() => setMessageBox(null)}
  //       />
  //     )}
  //   </div>
  // );
}
