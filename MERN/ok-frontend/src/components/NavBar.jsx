// Importations
import React, { useState } from "react";
import styled from "styled-components";
import { NavLink, Link } from "react-router-dom";
// Components Imports
import BurgerButton from "./BurgerButton";

function NavBar() {
  const [clicked, setClicked] = useState(false);

  const handleClick = () => {
    // Cuando esta true lo pasa a false y viceversa
    setClicked(!clicked);
  };

  return (
    <>
      <NavContainer>
        <h2>
          <span>
            <NavLink to="/">Orlando Korzo</NavLink>
          </span>
        </h2>
        <div className={`links ${clicked ? "activate" : ""}`}>
          <NavLink onClick={handleClick} to="projects">
            Projects
          </NavLink>
          <Link onClick={handleClick} to="awards">
            Awards
          </Link>
          <a onClick={handleClick} href="about-me">
            About Me
          </a>
          <a onClick={handleClick} href="contact-me">
            Contact Me
          </a>
        </div>
        <div className="burger">
          <BurgerButton clicked={clicked} handleClick={handleClick} />
        </div>
        <BgDiv className={`initial ${clicked ? "activate" : ""}`}></BgDiv>
      </NavContainer>
    </>
  );
}
export default NavBar;

const NavContainer = styled.nav`
  padding: 0.4rem;
  background-color: #333;
  display: flex;
  align-items: center;
  justify-content: space-between;

  h2 {
    span {
      font-weight: bold;
    }
    @media (max-width: 768px) {
      margin-left: 10rem;
    }
  }

  a {
    color: white;
    text-decoration: none;
    margin-right: 1rem;
  }
  .burger {
    @media (min-width: 768px) {
      display: none;
    }
  }
  .links {
    position: absolute;
    top: -700px;
    left: -2000px;
    right: 0;
    margin-left: auto;
    margin-right: auto;
    text-align: center;
    transition: all 0.5s ease;
    a {
      color: black;
      font-size: 2rem;
      display: block;
    }
    @media (min-width: 768px) {
      position: initial;
      margin: 0;
      a {
        font-size: 1rem;
        color: white;
        display: inline;
      }
    }
  }
  /**
    .links.activate {
      width: 100%;
      display: block;
      position: absolute;
      margin-left: auto;
      margin-right: auto;
      top: 30%;
      left: 0;
      right: 0;
      text-align: center;
      a {
        color: white;
        margin-top: 1rem;
        font-size: 2rem;
      }
    }
  */
`;

const BgDiv = styled.div`
  position: absolute;
  background-color: #222;
  top: -2000px;
  left: -2000px;
  height: 100%;
  z-index: -1;
  width: 100%;
  transition: all 0.6s ease;
  /**
    &.activate {
      border-radius: 0 0 100% 0;
      top: 0;
      left: 0;
      height: 100%;
      width: 100%;
    }
  */
`;
