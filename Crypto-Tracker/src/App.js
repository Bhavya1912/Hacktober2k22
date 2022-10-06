import React, {useState, useEffect} from "react";
import Coin from "./Coin";
import axios from 'axios';
import './App.css'



function App() {

const [search, setSearch] = useState('')
const [coins, setCoins] = useState([])

useEffect(()=>{
  axios.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false")


  .then(res=>{
    setCoins(res.data)
    })

  .catch(err=>{console.log("Oops, some error occured. Try again!")})
},[])



function handleChange(e){
  setSearch(e.target.value)
  
}

const filteredCoins = coins.filter(coin=>
  coin.name.toLowerCase().includes(search.toLowerCase()))




  return (
    <>
    <div className="credits">
      <p className="credits-first">Made with 💖 and 🍵 by</p>
    <p className="credits-name">&nbsp; <a href="https://github.com/mrb1nary">mrb1nary</a> </p>
    </div>
    <div className="App">
      <div className="coin-search">
        <h1 className="coin-text">Search a cryptocurrency</h1>
        <form>
          <input onChange={handleChange} type='text' className="coin-input"></input>
        </form>
        </div>
        {filteredCoins.map(coin=>{
        return <Coin
            key={coin.id} 
            name={coin.name}
            image={coin.image}
            symbol={coin.symbol}
            volume={coin.total_volume}
            price={coin.current_price}
            priceChange={coin.price_change_percentage_24h}
            marketCap={coin.market_cap}
          />
        
      })}
      
    </div>
    </>
  );
}

export default App;
