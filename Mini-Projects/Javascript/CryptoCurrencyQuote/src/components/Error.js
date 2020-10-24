import React from "react";
import PropTypes from "prop-types";
import styled from "styled-components";

const Mensaje = styled.div`
  background-color: #b7322c;
  padding: 1rem;
  color: #fff;
  font-size: 25px;
  text-transform: uppercase;
  font-weight: bold;
  text-align: center;
  font-family: "Bebas Neue", cursive;
`;

const Error = ({ mensaje }) => {
  return <Mensaje>{mensaje}</Mensaje>;
};

Error.prototype = {
  mensaje: PropTypes.string.isRequired,
};

export default Error;
