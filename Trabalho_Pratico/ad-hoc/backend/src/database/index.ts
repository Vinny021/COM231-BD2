import { createConnection, getConnection, getManager } from "typeorm";

export async function connect() {

     const conn = createConnection({
        name: 'default',
        type: 'postgres',
        host: 'localhost',
        port: 5432,
        username: 'postgres',
        password: 'postgres',
        database: 'pokemon',
        logging: true,
        entities: ['src/database/models/*.ts']
     });

    return conn;
}

