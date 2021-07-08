export interface Team {
    Abbreviation: string;
    City: string;
    Conference: string;
    Division: string;
    FullName: string;
    ID: number;
    Name: string;
}

export class Kvp {
    constructor() {}
    Key: string | undefined;
    Value: any | undefined;
}