import axios from "axios";
import { API } from "../const";

const options = {
  headers: {
    "Content-Type": "application/json",
  },
};

export const Register = async (body) => {
  try {
    const response = await axios.post(API + "user_reg/", body, options);
    console.log(response);
    return true;
  } catch (e) {
    console.error(e);
    return false;
  }
};

export const Log = async (body) => {
  try {
    const response = await axios.post(API + "user/token/login/", body, options);
    localStorage.setItem("Token", response.data.auth_token);
    console.log(response);
    window.location.reload();
  } catch (e) {
    console.error(e);
  }
};

export const Logout = async (body) => {
  try {
    const response = await axios.post(API + "user/token/logout/", body, {
      headers: {
        Authorization: `Token ${localStorage.Token}`,
      },
    });
    localStorage.removeItem("Token");
    console.log(response);
    window.location.reload();
  } catch (e) {
    console.log(e);
  }
};

export const getUsers = async () => {
  try {
    const response = await axios.get(API + "get_user_list", {
      headers: {
        Authorization: `Token ${localStorage.Token}`,
      },
    });
    return response.data.users;
  } catch (e) {
    console.log(e);
  }
};

export const createGame_req = async () => {
  try {
    const response = await axios.get(API + "start_game", {
      headers: {
        Authorization: `Token ${localStorage.Token}`,
      },
    });
    console.log(response);
    return response.data.game_code;
  } catch (e) {
    console.log(e);
    return null
  }
};

export const getGames = async () => {
  try {
    const response = await axios.get(API + "get_game_list", {
      headers: {
        Authorization: `Token ${localStorage.Token}`,
      },
    });
    return response.data;
  } catch (e) {
    console.log(e);
  }
};

export const createArea = async (body) => {
  try {
    const response = await axios.post(
      API + "create_area//",
      {
        game_code: localStorage.game_code + "",
        data: body,
      },
      {
        headers: {
          Authorization: `Token ${localStorage.Token}`,
        },
      }
    );
    console.log(response);
    if (response.statusText === "Created") {
      return true;
    }
  } catch (e) {
    console.log(e);
  }
};
