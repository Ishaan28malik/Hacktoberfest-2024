import React, { useState, useEffect } from "react";
import styled from "styled-components";
import Formulario from "./components/Formulario";
import Cotizacion from "./components/Cotizacion";
import Spinner from "./components/Spinner";
import Error from "./components/Error";
import Img from "./cryptomonedas.png";
import axios from "axios";

const Wrapper = styled.div`
  max-width: 900px;
  margin: 0 auto;
  @media (min-width: 992px) {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    column-gap: 2rem;
  }
`;

const Image = styled.img`
  max-width: 100%;
  margin-top: 5rem;
`;

const Heading = styled.h1`
  font-family: "Bebas Neue", cursive;
  color: #fff;
  text-align: left;
  font-weight: 700;
  font-size: 50px;
  margin-bottom: 50px;
  margin-top: 80px;
  &::after {
    content: "";
    width: 100px;
    height: 6px;
    background-color: #66a2fe;
    display: block;
  }
`;

function App() {
  const [cotizacion, setCotizacion] = useState({
    moneda: "",
    criptomoneda: "",
  });
  const { moneda, criptomoneda } = cotizacion;
  const [resultado, setResultado] = useState({});
  const [status, setStatus] = useState({
    spinner: false,
    error: false,
  });

  useEffect(() => {
    if (moneda === "" || criptomoneda === "") return;
    setStatus({ ...status, spinner: true });
    const getCotizacion = async () => {
      //consultar el api
      const url = `https://min-api.cryptocompare.com/data/pricemultifull?fsyms=${criptomoneda}&tsyms=${moneda}`;

      try {
        const response = await axios.get(url);
        setResultado(response.data.DISPLAY[criptomoneda][moneda]);
        setStatus({ spinner: false, error: false });
      } catch {
        setStatus({ spinner: false, error: true });
      }
    };
    getCotizacion();
    // eslint-disable-next-line
  }, [cotizacion]);

  const renderResultado = status.spinner ? (
    <Spinner />
  ) : (
    <Cotizacion resultado={resultado} />
  );

  return (
    <Wrapper>
      <div>
        <Image src={Img} alt="img" />
      </div>
      <div>
        <Heading>Cotiza criptomonedas al instante</Heading>
        <Formulario setCotizacion={setCotizacion} />
        {status.error ? (
          <Error mensaje="Estamos teniendo problemas de conexión :s vuelva a intentar" />
        ) : null}
        {renderResultado}
      </div>
    </Wrapper>
  );
}

export default App;
