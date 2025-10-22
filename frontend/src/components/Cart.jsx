import React from "react";
import API from "../services/api";

export default function Cart({ cartItems, closeCart, refreshCart }) {
  // Remove item from cart
  const removeItem = async (id) => {
    try {
      await API.delete(`/cart/remove/${id}`);
      refreshCart(); // refresh cart list
    } catch (err) {
      console.error("Failed to remove item:", err);
      alert("Failed to remove item from cart");
    }
  };

  // Checkout all items
  const checkout = async () => {
    try {
      const res = await API.post("/cart/checkout");
      alert(res.data.message || "Checkout successful!");
      refreshCart(); // refresh cart
      closeCart();   // close cart drawer
    } catch (err) {
      console.error("Checkout failed:", err);
      alert(err.response?.data?.detail || "Checkout failed");
    }
  };

  const total = cartItems.reduce(
    (sum, item) => sum + item.price * (item.quantity || 1),
    0
  );

  return (
    <div className="fixed top-0 right-0 w-80 h-full bg-white shadow-lg z-50 p-4 flex flex-col">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-bold text-amber-700">🛒 Cart</h2>
        <button onClick={closeCart} className="text-gray-500 hover:text-gray-700 text-xl">
          ✖
        </button>
      </div>

      {cartItems.length === 0 ? (
        <p className="text-gray-500 mt-10 text-center">Your cart is empty.</p>
      ) : (
        <div className="flex-1 overflow-y-auto">
          {cartItems.map((item) => (
            <div
              key={item.id}
              className="flex justify-between items-center border-b border-gray-200 py-2"
            >
              <div>
                <p className="font-semibold">{item.name}</p>
                <p className="text-gray-600 text-sm">
                  PKR {item.price.toFixed(2)} x {item.quantity || 1}
                </p>
              </div>
              <button
                onClick={() => removeItem(item.id)}
                className="text-red-500 hover:text-red-700"
              >
                🗑️
              </button>
            </div>
          ))}
        </div>
      )}

      {cartItems.length > 0 && (
        <div className="mt-4">
          <p className="font-bold text-lg text-right">Total: PKR {total.toFixed(2)}</p>
          <button
            onClick={checkout}
            className="w-full mt-2 bg-green-600 text-white py-2 rounded hover:bg-green-700 transition-transform active:scale-95"
          >
            Checkout
          </button>
        </div>
      )}
    </div>
  );
}
