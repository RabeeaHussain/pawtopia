import React, { useEffect, useState } from "react";
import API from "../services/api";
import { motion } from "framer-motion";

export default function Pets() {
  const [availablePets, setAvailablePets] = useState([]);
  const [adoptedPets, setAdoptedPets] = useState([]);
  const [message, setMessage] = useState("");

  // ✅ Fetch all pets (available + adopted)
  const fetchPets = async () => {
    try {
      const res = await API.get("/virtual_pets/");
      setAvailablePets(res.data.available || []);
      setAdoptedPets(res.data.adopted || []);
    } catch (err) {
      console.error("Error fetching pets:", err);
      setMessage("Failed to load pets.");
    }
  };

  useEffect(() => {
    fetchPets();
  }, []);

  // ✅ Adopt a pet
  const adoptPet = async (id) => {
    try {
      const res = await API.post(`/virtual_pets/adopt/${id}`);
      setMessage(`🎉 ${res.data.message}`);

      // Move the pet from available to adopted
      const adopted = availablePets.find((p) => p.id === id);
      if (!adopted) return;

      setAvailablePets(availablePets.filter((p) => p.id !== id));
      setAdoptedPets([
        ...adoptedPets,
        { ...adopted, happiness: adopted.happiness, energy: adopted.energy, hunger: adopted.hunger },
      ]);
    } catch (err) {
      console.error("Adoption failed:", err.response?.data || err);
      setMessage(err.response?.data?.detail || "Failed to adopt pet");
    }
  };

  return null;
  // return (
  //   <div className="p-6 max-w-6xl mx-auto">
  //     <h1 className="text-3xl font-bold text-center text-amber-700 mb-6">
  //       🐾 Virtual Pet Adoption
  //     </h1>

  //     {message && <p className="text-center text-green-600 mb-4">{message}</p>}

  //     <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
  //       {/* 🐕 Available Pets */}
  //       <div>
  //         <h2 className="text-2xl font-semibold text-amber-600 mb-4 text-center">
  //           🐶 Available Pets
  //         </h2>

  //         <div className="grid sm:grid-cols-2 gap-4">
  //           {availablePets.length > 0 ? (
  //             availablePets.map((p) => (
  //               <motion.div
  //                 key={p.id}
  //                 whileHover={{ scale: 1.03 }}
  //                 className="bg-white shadow-lg rounded-xl p-4 border border-gray-200"
  //               >
  //                 <h3 className="text-lg font-semibold text-amber-700">{p.name}</h3>
  //                 <p className="text-gray-600 text-sm mb-2 capitalize">
  //                   Species: {p.species}
  //                 </p>
  //                 <button
  //                   onClick={() => adoptPet(p.id)}
  //                   className="bg-amber-600 text-white w-full mt-2 py-1 rounded hover:bg-amber-700"
  //                 >
  //                   Adopt
  //                 </button>
  //               </motion.div>
  //             ))
  //           ) : (
  //             <p className="text-gray-500 text-center col-span-full">
  //               No available pets right now!
  //             </p>
  //           )}
  //         </div>
  //       </div>

  //       {/* 💖 Adopted Pets */}
  //       <div>
  //         <h2 className="text-2xl font-semibold text-green-600 mb-4 text-center">
  //           💖 My Adopted Pets
  //         </h2>

  //         <div className="grid sm:grid-cols-2 gap-4">
  //           {adoptedPets.length > 0 ? (
  //             adoptedPets.map((p) => (
  //               <motion.div
  //                 key={p.id}
  //                 whileHover={{ scale: 1.03 }}
  //                 className="bg-green-50 shadow-md rounded-xl p-4 border border-green-200"
  //               >
  //                 <h3 className="text-lg font-semibold text-green-800">{p.name}</h3>
  //                 <p className="text-gray-700 text-sm capitalize">Species: {p.species}</p>

  //                 {/* ✅ Pet stats */}
  //                 <div className="mt-2 text-sm text-gray-700">
  //                   <p>😊 Happiness: {p.happiness ?? 100}%</p>
  //                   <p>⚡ Energy: {p.energy ?? 100}%</p>
  //                   <p>🍗 Hunger: {p.hunger ?? 0}%</p>
  //                 </div>
  //               </motion.div>
  //             ))
  //           ) : (
  //             <p className="text-gray-500 text-center col-span-full">
  //               You haven’t adopted any virtual pets yet.
  //             </p>
  //           )}
  //         </div>
  //       </div>
  //     </div>
  //   </div>
  // );
}
