import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders input field alias", () => {
  render(<App />);
  const linkElement = screen.getByPlaceholderText(/alias/i);
  expect(linkElement).toBeInTheDocument();
});

test("renders input field url", () => {
  render(<App />);
  const linkElement = screen.getByPlaceholderText(/google/i);
  expect(linkElement).toBeInTheDocument();
});