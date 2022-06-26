import { connect } from '../database/index';
import { Request, Response } from "express";
import {getConnectionManager, getManager, getConnection} from "typeorm";

connect();
const manager = getManager();

export class PokemonController{
    async index(request: Request, response: Response){
        console.log(await manager.createQueryBuilder().select('*').from('northwind.orders', 'Order').getRawMany());
        const orders = await manager.createQueryBuilder().select('*').from('northwind.orders', 'Order').getRawMany();
        return response.status(200).send(orders)
    }
}