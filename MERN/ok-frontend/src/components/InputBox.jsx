// Importations
import React from "react";
import styled from "styled-components";

function InputBox({ label }) {
  return (
    <Box>
      <div className="input-group">
        <input id="box" type="text" className="input" />
        <label htmlFor="box" className="input-label">
          {label}
        </label>
      </div>
    </Box>
  );
}

export default InputBox;

const Box = styled.div`
  .input-group {
    position: relative;
    padding: 5px;
  }

  .input {
    padding: 10px;
    border: none;
    border-radius: 4px;
    outline: 3px solid black;
    background-color: white;
    width: 60%;
  }

  .input-label {
    position: absolute;
    top: 0;
    left: 0;
    transform: translate(10px, 10px);
    transform-origin: left;
    transition: transform 0.25s;
  }

  .input:focus + .input-label,
  .input:valid + .input-label {
    transform: translate(10px, -30px) scale (0.8);
  }

  .input:is(:focus, :valid) {
  }
`;
