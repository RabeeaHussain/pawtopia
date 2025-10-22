import React, { useEffect, useState } from "react";
import API from "../services/api";
import Cart from "../components/Cart";

export default function AdoptPets() {
  const [pets, setPets] = useState([]);
  const [message, setMessage] = useState("");
  const [showCart, setShowCart] = useState(false);
  const [cartItems, setCartItems] = useState([]);

  // ---------------- Fetch pets ----------------
  const fetchPets = async () => {
    try {
      // Fetch all pets, including adopted ones
      const res = await API.get("/pets"); 
      setPets(res.data);
    } catch (err) {
      console.error("Error fetching pets:", err);
      setPets([]);
      setMessage("Failed to load pets.");
    }
  };

  // ---------------- Fetch cart ----------------
  const fetchCart = async () => {
    try {
      const res = await API.get("/cart/");
      setCartItems(res.data.cart || []);
    } catch (err) {
      console.error("Failed to fetch cart:", err);
      setCartItems([]);
      setMessage("Failed to load cart.");
    }
  };

  // ---------------- Adopt a pet ----------------
  const adoptPet = async (id) => {
    try {
      const res = await API.post(`/pets/${id}/adopt`);
      setMessage(res.data.message);
      fetchPets();
      fetchCart();
    } catch (err) {
      console.error("Error adopting pet:", err);
      setMessage(err.response?.data?.detail || "Failed to adopt pet.");
    }
  };

  // ---------------- Unadopt a pet ----------------
  const unadoptPet = async (id) => {
    try {
      const res = await API.post(`/pets/${id}/unadopt`);
      setMessage(res.data.message);
      fetchPets();
      fetchCart();
    } catch (err) {
      console.error("Error unadopting pet:", err);
      setMessage(err.response?.data?.detail || "Failed to unadopt pet.");
    }
  };

  // ---------------- Buy a product ----------------
  const buyProduct = async (productId, name) => {
    try {
      const res = await API.post(`/cart/add_product/${productId}`);
      alert(res.data.message || `${name} added to cart!`);
      fetchCart();
    } catch (err) {
      console.error("Failed to add product to cart:", err);
      alert(err.response?.data?.detail || "Failed to add to cart");
    }
  };

  useEffect(() => {
    fetchPets();
    fetchCart();
  }, []);

  // ---------------- Split pets ----------------
  const adoptedPets = pets.filter((p) => p.is_adopted);
  const availablePets = pets.filter((p) => !p.is_adopted);

  return null;
  // return (
  //   <div className="p-6 max-w-4xl mx-auto text-center">
  //     {/* Header with Cart */}
  //     <header className="flex justify-between items-center mb-6">
  //       <h1 className="text-3xl font-bold text-amber-700">🐾 Adopt a Pet</h1>
  //       <button
  //         onClick={() => setShowCart(true)}
  //         className="text-3xl text-amber-700 hover:text-amber-800 relative"
  //         title="View Cart"
  //       >
  //         🛒
  //         {cartItems.length > 0 && (
  //           <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs w-5 h-5 flex items-center justify-center rounded-full">
  //             {cartItems.length}
  //           </span>
  //         )}
  //       </button>
  //     </header>

  //     {/* Status message */}
  //     {message && <p className="mb-4 text-green-600">{message}</p>}

  //     {/* Available Pets */}
  //     <section className="mb-8">
  //       <h2 className="text-2xl font-bold mb-4 text-amber-700">Available Pets</h2>
  //       {availablePets.length > 0 ? (
  //         availablePets.map((pet) => (
  //           <div
  //             key={pet.id}
  //             className="bg-white shadow rounded-lg p-4 mb-4 flex justify-between items-center"
  //           >
  //             <div>
  //               <h3 className="text-xl font-semibold">{pet.name}</h3>
  //               <p className="text-gray-600">
  //                 {pet.species} — PKR {pet.price.toFixed(2)}
  //               </p>
  //             </div>
  //             <div className="flex gap-2">
  //               <button
  //                 onClick={() => adoptPet(pet.id)}
  //                 className="bg-amber-600 text-white px-4 py-2 rounded hover:bg-amber-700 transition-transform active:scale-95"
  //               >
  //                 Adopt
  //               </button>
  //               <button
  //                 onClick={() => buyProduct(pet.id, pet.name)}
  //                 className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition-transform active:scale-95"
  //               >
  //                 Buy
  //               </button>
  //             </div>
  //           </div>
  //         ))
  //       ) : (
  //         <p className="text-gray-500">No pets available for adoption right now.</p>
  //       )}
  //     </section>

  //     {/* Adopted Pets */}
  //     <section className="mb-8">
  //       <h2 className="text-2xl font-bold mb-4 text-amber-700">Your Adopted Pets</h2>
  //       {adoptedPets.length > 0 ? (
  //         adoptedPets.map((pet) => (
  //           <div
  //             key={pet.id}
  //             className="bg-white shadow rounded-lg p-4 mb-4 flex justify-between items-center"
  //           >
  //             <div>
  //               <h3 className="text-xl font-semibold">{pet.name}</h3>
  //               <p className="text-gray-600">
  //                 {pet.species} — PKR {pet.price.toFixed(2)}
  //               </p>
  //             </div>
  //             <button
  //               onClick={() => unadoptPet(pet.id)}
  //               className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 transition-transform active:scale-95"
  //             >
  //               Unadopt
  //             </button>
  //           </div>
  //         ))
  //       ) : (
  //         <p className="text-gray-500">You have not adopted any pets yet.</p>
  //       )}
  //     </section>

  //     {/* Cart Drawer */}
  //     {showCart && (
  //       <Cart
  //         cartItems={cartItems}
  //         closeCart={() => setShowCart(false)}
  //         refreshCart={fetchCart}
  //       />
  //     )}
  //   </div>
  // );
}
