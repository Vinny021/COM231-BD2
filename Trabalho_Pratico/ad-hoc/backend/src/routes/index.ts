import { Router } from "express";
import { connect } from '../database/index';
import {getConnectionManager, getManager, getConnection} from "typeorm";
import { PokemonController } from '../controllers/PokemonController';

connect();
const manager = getManager();


const routes = Router();
// const connection = getConnection();
routes
  .route("/")
  .get(new PokemonController().index);

  
export { routes };
