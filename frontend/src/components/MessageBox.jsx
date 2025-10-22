import React, { useEffect } from "react";

export default function MessageBox({ message, type = "info", onClose }) {
  if (!message) return null;

  const bgColor =
    type === "success"
      ? "bg-green-100 border-green-400 text-green-700"
      : type === "error"
      ? "bg-red-100 border-red-400 text-red-700"
      : "bg-blue-100 border-blue-400 text-blue-700";

  const icon =
    type === "success" ? "✅" : type === "error" ? "❌" : "ℹ️";

  useEffect(() => {
    const timer = setTimeout(onClose, 4000);
    return () => clearTimeout(timer);
  }, [message, onClose]);

  return (
    <div className="fixed top-4 left-1/2 transform -translate-x-1/2 z-50 w-full max-w-sm">
      <div className={`flex items-start p-4 border rounded-xl shadow-xl ${bgColor}`}>
        <span className="text-xl mr-3">{icon}</span>
        <div className="flex-grow">
          <p className="font-semibold capitalize">{type}</p>
          <p className="text-sm">{message}</p>
        </div>
        <button onClick={onClose} className="ml-3 text-lg font-bold">
          &times;
        </button>
      </div>
    </div>
  );
}
