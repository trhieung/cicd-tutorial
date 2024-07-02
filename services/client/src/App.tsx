import React, { useState } from "react";
// import reactLogo from "./assets/react.svg";
// import viteLogo from "/vite.svg";

import { A_Component } from "./components/Icons";
// Import all images from the public/images directory
// const images = import.meta.glob("/public/images/*.png", { eager: true });

import "./App.css";

const AppHeader: React.FC = () => {
  const [activeMenuLink, setActiveMenuLink] = useState<string>("Apps");

  const handleMenuClick = (menuName: string) => {
    setActiveMenuLink(menuName);
  };

  return (
    <div className="header">
      <div className="menu-circle"></div>
      <div className="header-menu">
        <a
          className={`menu-link ${
            activeMenuLink === "Apps" ? "is-active" : ""
          }`}
          href="#"
          onClick={() => handleMenuClick("Apps")}
        >
          Apps
        </a>
        <a
          className={`menu-link notify ${
            activeMenuLink === "Your work" ? "is-active" : ""
          }`}
          href="#"
          onClick={() => handleMenuClick("Your work")}
        >
          Your work
        </a>
        <a
          className={`menu-link ${
            activeMenuLink === "Discover" ? "is-active" : ""
          }`}
          href="#"
          onClick={() => handleMenuClick("Discover")}
        >
          Discover
        </a>
        <a
          className={`menu-link notify ${
            activeMenuLink === "Market" ? "is-active" : ""
          }`}
          href="#"
          onClick={() => handleMenuClick("Market")}
        >
          Market
        </a>
      </div>
      <div className="search-bar">
        <input type="text" placeholder="Search" />
      </div>
      <div className="header-profile"></div>
    </div>
  );
};

// function

function AppWrapperLeftside() {
  const items = {
    // Apps: ["baby", "huhu"],
    Categories: [
      "Amazon_Instant_Video",
      "Apps_for_Android",
      "Automotive",
      "Baby",
      "Beauty",
      "Books",
      "CDs_and_Vinyl",
      "Cell_Phones_and_Accessories",
      "Clothing_Shoes_and_Jewelry",
      "Digital_Music",
      "Electronics",
      "Grocery_and_Gourmet_Food",
      "Health_and_Personal_Care",
      "Home_and_Kitchen",
      "Kindle_Store",
      "Movies_and_TV",
      "Musical_Instruments",
      "Office_Products",
      "Patio_Lawn_and_Garden",
      "Pet_Supplies",
      "Sports_and_Outdoors",
      "Tools_and_Home_Improvement",
      "Toys_and_Games",
      "Video_Games",
    ],
  };

  const items_with_ref = {
    Resource: [
      ["Git", "youtube.com"],
      [
        "Drive",
        "https://drive.google.com/drive/folders/1EfJXnMkj-ht25NU-9YTFCwZMCIRPl0p_?usp=sharing",
      ],
      ["Kaggle", "https://www.kaggle.com/"],
      ["Hugging_Face", "https://huggingface.co/nthieu"],
    ],
    Reference: [
      [
        "Tutorials",
        "https://www.tensorflow.org/text/tutorials/classify_text_with_bert",
      ],
      ["Social_Forum", "youtube.com"],
    ],
  };

  return (
    <div className="left-side">
      {Object.entries(items).map(([title, names], index) => (
        <div key={index} className="side-wrapper">
          <div className="side-title">{title}</div>
          <div className="side-menu">
            {names.map((name, idx) => (
              <A_Component key={idx} selectedItem={name} />
            ))}
          </div>
        </div>
      ))}
      {Object.entries(items_with_ref).map(([title, refs], index) => (
        <div key={index + Object.keys(items).length} className="side-wrapper">
          <div className="side-title">{title}</div>
          <div className="side-menu">
            {refs.map(([name, href], idx) => (
              <A_Component key={idx} selectedItem={name} href={href} />
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

const ContentWrapperHeader: React.FC = () => {
  const [usernames, setUsernames] = useState<string[]>([]);

  const fetchData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/users/");
      const data = await response.json();
      console.table(data);
      setUsernames(data.results.map((user: any) => user.username));
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleGenerateCommentClick = () => {
    fetchData();
  };

  return (
    <div className="content-wrapper">
      <div className="content-wrapper-header">
        <div className="content-wrapper-context">
          <h3 className="img-content" id="categoryTitle">
            Categories
          </h3>

          <div className="content-text">
            {usernames.length > 0 ? (
              <ul>
                {usernames.map((username, index) => (
                  <li key={index}>{username}</li>
                ))}
              </ul>
            ) : (
              "Grab yourself 10 free images to help you with your new project."
            )}
          </div>
          <button
            id="generateCommentButton"
            className="content-button"
            onClick={handleGenerateCommentClick}
          >
            Generate comment
          </button>
        </div>
        <img
          className="content-wrapper-img"
          src="../public/images/image0.png"
          alt="description"
        />
      </div>
    </div>
  );
};

export default ContentWrapperHeader;

const ContentSection1: React.FC = () => {
  return <></>;
};

function ContentSection2() {
  return <></>;
}

function AppWrapperMainContainer() {
  return (
    <>
      <div className="main-container">
        <div className="main-header">
          <a className="menu-link-main" href="#">
            Hoc thong ke
          </a>
          <div className="header-menu">
            <a className="main-header-link is-active" href="#">
              Amazone Product Predict Model
            </a>
          </div>
        </div>
        <ContentWrapperHeader />
        <ContentSection1 />
        <ContentSection2 />
      </div>
    </>
  );
}

function AppWrapper() {
  return (
    <div className="wrapper">
      <AppWrapperLeftside />
      <AppWrapperMainContainer />
    </div>
  );
}

function AppOverlay() {
  return <div className="overlay-app"></div>;
}

function App() {
  return (
    <div className="app">
      <AppHeader />
      <AppWrapper />
      <AppOverlay />
    </div>
  );
}

function Cover() {
  return (
    <div className="video-bg">
      <video width="750" height="500" autoPlay loop muted>
        <source
          src="https://assets.codepen.io/3364143/7btrrd.mp4"
          type="video/mp4"
        />
        huhu
      </video>
    </div>
  );
}

function ThemeChange() {
  return (
    <div className="dark-light">
      <svg
        viewBox="0 0 24 24"
        stroke="currentColor"
        stroke-width="1.5"
        fill="none"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" />
      </svg>
    </div>
  );
}

export { App, Cover, ThemeChange };
