import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
//import { ArrowRight, ShoppingBag, PawPrint } from 'lucide-react';
import Navbar from '../components/Navbar';
//import { supabase } from '../lib/supabase';

const COLOR_GOLD = '#B58E4A';
const COLOR_CREAM = '#FFF8E0';
const COLOR_NAV_BG = '#cc8528';
const COLOR_NAV_TEXT = '#774e18';



export default function Home() {
  const [realPets, setRealPets] = useState([]);
  const [virtualPets, setVirtualPets] = useState([]);
  const [loading, setLoading] = useState(false);

  // useEffect(() => {
  //   const fetchAll = async () => {
  //     try {
  //       const [petsRes, virtualRes] = {}
  //       // await Promise.all([
  //       //   supabase.from('pets').select('*').eq('available', true).limit(3),
  //       //   supabase.from('virtual_pets').select('*').is('user_id', null).limit(3),
  //       // ]);

  //       if (petsRes.data) setRealPets(petsRes.data);
  //       if (virtualRes.data) setVirtualPets(virtualRes.data);
  //     } catch (err) {
  //       console.error('Error fetching pets:', err);
  //     } finally {
  //       setLoading(false);
  //     }
  //   };
  //   fetchAll();
  // }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen text-xl font-semibold" style={{ backgroundColor: COLOR_CREAM, color: COLOR_GOLD }}>
        {/* <PawPrint className="animate-pulse mr-3" size={28} /> Loading Pawtopia... */}
      </div>
    );
  }

  return (
    <div style={{ backgroundColor: COLOR_CREAM, minHeight: '100vh' }}>
      <Navbar />

      <div className="pt-20">
        <section className="text-center py-20 px-4">
          <h1
            className="text-6xl md:text-7xl font-bold mb-4 tracking-tight font-serif italic"
            style={{ color: COLOR_NAV_TEXT }}
          >
            Welcome to Pawtopia
          </h1>
          <p className="text-xl max-w-3xl mx-auto opacity-90 font-light mb-12" style={{ color: COLOR_NAV_TEXT }}>
            Adopt real pets, care for virtual companions, and shop for all your furry friends in one happy place.
          </p>

          <div className="flex justify-center mt-8">
            <div className="w-4/5 md:w-1/3 h-px relative" style={{ backgroundColor: COLOR_GOLD }}>
              <div
                className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-4 h-4 rounded-full border-2 shadow-sm"
                style={{ backgroundColor: COLOR_GOLD, borderColor: COLOR_CREAM }}
              ></div>
            </div>
          </div>
        </section>

        <section className="max-w-7xl mx-auto py-16 px-6 md:px-8 my-16 rounded-3xl shadow-2xl" style={{ backgroundColor: 'white' }}>
          <div className="flex justify-between items-center mb-8 pb-4 px-6 rounded-t-3xl" style={{ backgroundColor: COLOR_NAV_BG }}>
            <h2 className="text-4xl tracking-tight font-serif italic py-4" style={{ color: COLOR_NAV_TEXT }}>
              Adopt Your Virtual Pet
            </h2>
            <Link to="/virtual" className="flex items-center gap-1 text-lg font-medium hover:text-white transition" style={{ color: COLOR_NAV_TEXT }}>
              Explore 
              {/* <ArrowRight size={18} /> */}
            </Link>
          </div>

          {virtualPets.length === 0 ? (
            <p className="text-center text-xl py-8 opacity-90" style={{ color: COLOR_NAV_TEXT }}>
              No virtual pets available 
              {/* <PawPrint size={20} className="inline ml-1" /> */}
            </p>
          ) : (
            <div className="flex gap-6 justify-between w-full px-6 pb-6">
              {virtualPets.map((pet) => (
                <div
                  key={pet.id}
                  className="flex-1 bg-white rounded-xl p-6 shadow-xl border border-gray-200 flex flex-col justify-between transition duration-300 hover:shadow-2xl hover:scale-[1.02] transform"
                  style={{ minHeight: '200px' }}
                >
                  <div>
                    <h3 className="text-2xl font-extrabold" style={{ color: COLOR_NAV_TEXT }}>
                      {pet.name}
                    </h3>
                    <p className="italic text-sm text-gray-500 mb-4">{pet.species}</p>
                  </div>
                  <div className="space-y-1" style={{ color: COLOR_NAV_TEXT }}>
                    <p>Hunger: <span className="font-semibold">{pet.hunger}</span></p>
                    <p>Energy: <span className="font-semibold">{pet.energy}</span></p>
                    <p>Happiness: <span className="font-semibold">{pet.happiness}</span></p>
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>

        <section className="max-w-7xl mx-auto py-16 px-6 md:px-8">
          <div className="flex justify-between items-center mb-8 pb-3 px-6 rounded-t-xl" style={{ backgroundColor: COLOR_NAV_BG }}>
            <h2 className="text-4xl tracking-tight font-serif italic py-4" style={{ color: COLOR_NAV_TEXT }}>
              Real Pets for Adoption
            </h2>
            <Link to="/adopt" className="flex items-center gap-1 text-lg font-medium hover:text-white transition" style={{ color: COLOR_NAV_TEXT }}>
              View All 
              {/* <ArrowRight size={18} /> */}
            </Link>
          </div>

          {realPets.length === 0 ? (
            <p className="text-center text-xl py-8 opacity-80" style={{ color: COLOR_NAV_TEXT }}>
              No real pets available at the moment 
              {/* <PawPrint size={20} className="inline ml-1" /> */}
            </p>
          ) : (
            <div className="flex gap-6">
              {realPets.map((pet) => (
                <div
                  key={pet.id}
                  className="flex-1 bg-white rounded-xl shadow-lg overflow-hidden transition duration-300 transform hover:shadow-2xl hover:scale-[1.02] border border-gray-100 flex flex-col justify-between"
                  style={{ minHeight: '250px' }}
                >
                  <div className="p-6" style={{ color: COLOR_NAV_TEXT }}>
                    <h3 className="text-2xl font-extrabold" style={{ color: COLOR_NAV_TEXT }}>{pet.name}</h3>
                    <p className="text-sm text-gray-500 mt-1 italic font-light">{pet.species}</p>
                    <div className="mt-4 pt-3 border-t border-gray-100 space-y-2 text-base">
                      <p><span className="font-semibold">Age:</span> {pet.age || 'Unknown'}</p>
                      <p className="text-2xl font-bold" style={{ color: COLOR_NAV_TEXT }}>
                        <span className="text-sm font-medium align-top">$</span>{pet.price}
                      </p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>

        <section className="max-w-7xl mx-auto py-16 px-6 md:px-8 text-center pb-32">
          <h2 className="text-4xl mb-4 tracking-tight font-serif italic" style={{ color: COLOR_NAV_TEXT }}>
            Need Pet Supplies?
          </h2>
          <p className="text-xl mb-8 max-w-3xl mx-auto opacity-90" style={{ color: COLOR_NAV_TEXT }}>
            Visit our shop for high-quality toys, nourishing food, and essential accessories your pets will love.
          </p>
          <Link
            to="/shop"
            className="inline-flex items-center gap-2 px-10 py-4 rounded-full text-lg font-semibold shadow-xl hover:shadow-2xl transition duration-300 transform hover:-translate-y-0.5"
            style={{ backgroundColor: COLOR_GOLD, color: COLOR_CREAM }}
          >
            {/* <ShoppingBag size={20} /> Visit Shop */}
          </Link>
        </section>
      </div>
    </div>
  );
}
