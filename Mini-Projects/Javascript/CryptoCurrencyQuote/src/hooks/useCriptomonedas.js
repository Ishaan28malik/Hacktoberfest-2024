import React, { useState, Fragment } from "react";
import PropType from "prop-types";
import styled from "styled-components";

const Label = styled.label`
  font-family: "Bebas Neue", cursive;
  color: #fff;
  text-transform: uppercase;
  font-weight: bold;
  font-size: 2.4rem;
  margin-top: 2rem;
  display: block;
`;

const Select = styled.select`
  width: 100%;
  display: block;
  padding: 1rem;
  -webkit-appearance: none;
  border-radius: 10px;
  border: none;
  font-size: 1.2rem;
`;

const useCriptomonedas = (label, opciones) => {
  //state de custom Hook
  const [criptomoneda, setCriptomoneda] = useState("");

  const SeleccionarCripto = () => (
    <Fragment>
      <Label>{label}</Label>
      <Select
        value={criptomoneda}
        onChange={(e) => setCriptomoneda(e.target.value)}
      >
        <option value="">---Seleccione---</option>
        {opciones.map((opcion) => (
          <option key={opcion.CoinInfo.Id} value={opcion.CoinInfo.Name}>
            {opcion.CoinInfo.FullName}
          </option>
        ))}
      </Select>
    </Fragment>
  );

  //Retornar state, interfaz, función que modifica el state
  return [criptomoneda, SeleccionarCripto];
};

useCriptomonedas.prototype = {
  label: PropType.string.isRequired,
  opciones: PropType.array.isRequired,
};

export default useCriptomonedas;
