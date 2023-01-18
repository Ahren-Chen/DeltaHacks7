import React from "react";
import "./App.css";
import Graylogo from "./images/GRAY.png";
import OpenNow from "./images/OpenNow.png";
import Phone from "./images/phone.png";
import { Link } from "react-router-dom";
function Home() {
  return (
    <div className="background">
      <div className="title">
        <img src={Graylogo} style={{ height: 50, width: 60 }} />
        <div className="companyName">G.R.A.Y GROUP</div>
      </div>
      <div className="backgroundTwo">
        <div className="openNowWrapper">
          <div className="stackText">
            <div className="ShopLocal">LOCAL LOVE</div>
            <div className="findBusinesses">Find Local Businesses Near you</div>
          </div>
          <div className="openNow">
            <img src={OpenNow} style={{ height: 342, width: 530 }} />
          </div>
        </div>
      </div>
      <div className="backgroundThree">
        <img src={Phone} style={{ height: 275, width: 412.5 }} />
        <div className="stackTextTwo">
          <div className="enterLocation">1. Enter Your Location</div>
          <div className="enterLocation">2. Type In What Food You Want</div>
          <div className="buttonWrapper">
            <Link className="button" to="/Map">
              TRY NOW
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
