import React, { Fragment, useState } from "react";
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

const useMoneda = (label, opciones) => {
  //state de custom Hook
  const [moneda, setMoneda] = useState("");

  const SeleccionarMoneda = () => (
    <Fragment>
      <Label>{label}</Label>
      <Select value={moneda} onChange={(e) => setMoneda(e.target.value)}>
        <option value="">---Seleccione---</option>
        {opciones.map((opcion) => (
          <option key={opcion.codigo} value={opcion.codigo}>
            {opcion.nombre}
          </option>
        ))}
      </Select>
    </Fragment>
  );

  //Retornar state, interfaz, función que modifica el state
  return [moneda, SeleccionarMoneda];
};

useMoneda.prototype = {
  label: PropType.string.isRequired,
  opciones: PropType.array.isRequired,
};

export default useMoneda;
