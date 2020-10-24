import React, { useState, useEffect } from "react";
import PropType from "prop-types";
import styled from "styled-components";
import axios from "axios";

import Error from "./Error";
import useMoneda from "../hooks/useMoneda";
import useCriptomonedas from "../hooks/useCriptomonedas";

const Btn = styled.input`
  margin-top: 20px;
  font-weight: bold;
  font-size: 20px;
  padding: 20px;
  background-color: #66a2fe;
  border: none;
  width: 100%;
  border-radius: 10px;
  color: #fff;
  transition: background-color 0.3s ease;
  &:hover {
    background-color: #326ac0;
    cursor: pointer;
  }
`;

const Formulario = ({ setCotizacion }) => {
  // state del listado de criptomonedas
  const [listaCripto, setListaCripto] = useState([]);
  const [error, setError] = useState(false);

  const MONEDAS = [
    { codigo: "USD", nombre: "Dolar de Estados Unidos" },
    { codigo: "MXN", nombre: "Peso Méxicano" },
    { codigo: "EUR", nombre: "Euro" },
    { codigo: "GBP", nombre: "Libra Esterlina" },
  ];
  //utilizando el useMoneda- orden del array [state, interfaz setState]
  const [moneda, SelectMoneda] = useMoneda("Elige tu moneda", MONEDAS);
  const [criptomoneda, SelectCriptomoneda] = useCriptomonedas(
    "Elige tu critomoneda",
    listaCripto
  );

  //cuando el usuario haga submit
  const cotizarMoneda = (e) => {
    e.preventDefault();
    //validar si los campos estan llenos
    if (moneda === "" || criptomoneda === "") {
      setError(true);
      return;
    }

    //En caso contrario pasar los datos al componente principal
    setCotizacion({
      moneda,
      criptomoneda,
    });
    setError(false);
  };

  //llamado a la api
  useEffect(() => {
    const consultarAPI = async () => {
      const url =
        "https://min-api.cryptocompare.com/data/top/mktcapfull?limit=10&tsym=USD";
      const res = await axios.get(url);
      setListaCripto(res.data.Data);
    };
    consultarAPI();
  }, []);

  return (
    <form onSubmit={cotizarMoneda}>
      {error ? <Error mensaje="Todos los campos son obligatorios" /> : null}
      <SelectMoneda />
      <SelectCriptomoneda />
      <Btn type="submit" value="calcular" />
    </form>
  );
};

Formulario.prototype = {
  setCotizacion: PropType.func.isRequired,
};

export default Formulario;
