import React from "react";
import propTypes from "prop-types";
import "./index.scss";

export default function Star({ className, value, height, width, spacing }) {
  const decimals = Number(value) % 1;
  const star = [];
  let leftPost = 0;
  for (let i = 0; i < 5 && i < value - decimals; i++) {
    leftPost = leftPost + width;
    star.push(
      <div
        className="star"
        key={`star-${i}`}
        style={{
          left: i * width,
          height: height,
          width: width,
          marginRight: spacing,
        }}
      ></div>
    );
  }

  if (decimals > 0 && value <= 5) {
    star.push(
      <div
        className="star"
        key={`starWithDecimals`}
        style={{
          left: leftPost,
          width: decimals * width - spacing,
          height: height,
        }}
      ></div>
    );
  }

  const starPlaceholder = [];

  for (let i = 0; i < 5; i++) {
    star.push(
      <div
        className="star placeholder"
        key={`starPlaceholder-${i}`}
        style={{
          left: i * width,
          height: height,
          width: width,
          marginRight: spacing,
        }}
      ></div>
    );
  }

  return (
    <>
      <div
        className={["stars", className].join(" ")}
        style={{ height: height }}
      >
        {starPlaceholder}
        {star}
      </div>
    </>
  );
}

Star.propTypes = {
  className: propTypes.string,
  value: propTypes.number,
  height: propTypes.number,
  width: propTypes.number,
  spacing: propTypes.number,
};

/* Example 

  <Star value={data.rate} width={35} height={35} spacing={4} />

*/
