import { Link, useLocation } from 'react-router-dom';

const COLOR_GOLD = '#B58E4A';
const COLOR_NAV_TEXT = '#774e18';
const COLOR_NAV_BG = '#cc8528';

export default function Navbar() {
  const navLinks = [
    { name: 'Home', path: '/' },
    { name: 'Virtual Pets', path: '/virtual' },
    { name: 'Adopt a Pet', path: '/adopt' },
    { name: 'Products', path: '/shop' },
  ];

  const location = useLocation();

  return (
    <nav className="w-full h-20 fixed top-0 z-50" style={{ backgroundColor: COLOR_NAV_BG }}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full">
        <div className="flex justify-between h-full items-center">
          <Link to="/" className="text-2xl font-serif italic tracking-wide" style={{ color: COLOR_NAV_TEXT }}>
            Pawtopia
          </Link>

          <div className="flex gap-6">
            {navLinks.map((link) => {
              const isActive = location.pathname === link.path;
              return (
                <Link
                  key={link.name}
                  to={link.path}
                  className="px-6 py-3 rounded transition duration-300"
                  style={{
                    color: isActive ? COLOR_GOLD : COLOR_NAV_TEXT,
                    fontSize: 18,
                    fontWeight: isActive ? 'bold' : 'normal',
                  }}
                >
                  {link.name}
                </Link>
              );
            })}
          </div>

          <Link
            to="/login"
            className="px-4 py-2 text-sm font-medium rounded-full shadow-md transition duration-300 hover:shadow-lg transform hover:-translate-y-px"
            style={{ backgroundColor: COLOR_NAV_BG, color: COLOR_NAV_TEXT }}
          >
            Login / Signup
          </Link>
        </div>
      </div>
    </nav>
  );
}
