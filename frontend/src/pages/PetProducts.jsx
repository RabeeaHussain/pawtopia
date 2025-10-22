import React, { useEffect, useState } from "react";
import API from "../services/api";
import Cart from "../components/Cart";

export default function PetProducts() {
  const [products, setProducts] = useState([]);
  const [showCart, setShowCart] = useState(false);
  const [cartItems, setCartItems] = useState([]);

  // Fetch available products
  const fetchProducts = async () => {
    try {
      const res = await API.get("/products");
      setProducts(res.data);
    } catch (err) {
      console.error("Error loading products:", err);
    }
  };

  // Fetch cart items
  const fetchCart = async () => {
    try {
      const res = await API.get("/cart/");
      setCartItems(res.data.cart || []);
    } catch (err) {
      console.error("Failed to fetch cart:", err);
      setCartItems([]);
    }
  };

  const addToCart = async (product) => {
    try {
      await API.post(`/cart/add_product/${product.id}`);
      alert(`${product.name} added to cart!`);
      fetchCart(); // refresh cart badge
    } catch (err) {
      console.error(err);
      alert(err.response?.data?.detail || "Failed to add to cart");
    }
  };

  useEffect(() => {
    fetchProducts();
    fetchCart();
  }, []);

  return null;
  // return (
  //   <div className="p-6 max-w-4xl mx-auto">
  //     {/* Header with Cart Icon */}
  //     <header className="flex justify-between items-center mb-6">
  //       <h1 className="text-3xl font-bold text-amber-700">🛍️ Shop Pet Products</h1>
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

  //     {products.length > 0 ? (
  //       <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
  //         {products.map((product) => (
  //           <div
  //             key={product.id}
  //             className="bg-white shadow rounded-lg p-4 flex flex-col justify-between"
  //           >
  //             <div>
  //               <h2 className="text-xl font-semibold">{product.name}</h2>
  //               <p className="text-gray-600">{product.category}</p>
  //               <p className="text-gray-700 mt-1">PKR {product.price.toFixed(2)}</p>
  //             </div>
  //             <button
  //               onClick={() => addToCart(product)}
  //               className="mt-4 bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition-transform active:scale-95"
  //             >
  //               Add to Cart
  //             </button>
  //           </div>
  //         ))}
  //       </div>
  //     ) : (
  //       <p className="text-gray-500 text-center">No products available right now.</p>
  //     )}

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
