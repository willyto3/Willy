// Importations
import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { ThemeProvider } from "styled-components";

// Pages Imports
import { MainPage, ProjectsPage, ProjectPage } from "./exports";

// Components Imports
import { Themes, InputBox, NavBar, Footer } from "./exports";

export default function App() {
  return (
    <>
      <BrowserRouter>
        <ThemeProvider theme={Themes["ligth"]}>
          <div className="App">
            <NavBar />
            <br />

            <Routes>
              <Route path="/" element={<MainPage />} />
              <Route path="/projects" element={<ProjectsPage />} />
              <Route path="/projects/:id" element={<ProjectPage />} />
              <Route path="/awards" element={<InputBox label="AWARDS" />} />
              <Route path="/about-me" element={<InputBox label="ABOUT ME" />} />
              <Route
                path="/contact-me"
                element={<InputBox label="CONTACT ME" />}
              />
              <Route path="*" element={<InputBox label="404" />} />
            </Routes>
          </div>
          <Footer />
        </ThemeProvider>
      </BrowserRouter>
    </>
  );
}

