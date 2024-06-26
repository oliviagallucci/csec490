/* tslint:disable */
/* eslint-disable */
/**
 * CSEC 490 API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface Class
 */
export interface Class {
    /**
     * 
     * @type {string}
     * @memberof Class
     */
    id?: string;
    /**
     * 
     * @type {string}
     * @memberof Class
     */
    name: string;
    /**
     * 
     * @type {string}
     * @memberof Class
     */
    slug?: string;
    /**
     * 
     * @type {boolean}
     * @memberof Class
     */
    visible?: boolean;
}

/**
 * Check if a given object implements the Class interface.
 */
export function instanceOfClass(value: object): boolean {
    if (!('name' in value)) return false;
    return true;
}

export function ClassFromJSON(json: any): Class {
    return ClassFromJSONTyped(json, false);
}

export function ClassFromJSONTyped(json: any, ignoreDiscriminator: boolean): Class {
    if (json == null) {
        return json;
    }
    return {
        
        'id': json['id'] == null ? undefined : json['id'],
        'name': json['name'],
        'slug': json['slug'] == null ? undefined : json['slug'],
        'visible': json['visible'] == null ? undefined : json['visible'],
    };
}

export function ClassToJSON(value?: Class | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'uuid': value['id'],
        'name': value['name'],
        'slug': value['slug'],
        'visible': value['visible'],
    };
}

