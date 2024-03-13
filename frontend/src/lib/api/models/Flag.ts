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
 * @interface Flag
 */
export interface Flag {
    /**
     * 
     * @type {string}
     * @memberof Flag
     */
    uuid?: string;
    /**
     * 
     * @type {string}
     * @memberof Flag
     */
    style?: string;
    /**
     * 
     * @type {string}
     * @memberof Flag
     */
    config?: string;
    /**
     * 
     * @type {number}
     * @memberof Flag
     */
    points?: number;
}

/**
 * Check if a given object implements the Flag interface.
 */
export function instanceOfFlag(value: object): boolean {
    return true;
}

export function FlagFromJSON(json: any): Flag {
    return FlagFromJSONTyped(json, false);
}

export function FlagFromJSONTyped(json: any, ignoreDiscriminator: boolean): Flag {
    if (json == null) {
        return json;
    }
    return {
        
        'uuid': json['uuid'] == null ? undefined : json['uuid'],
        'style': json['style'] == null ? undefined : json['style'],
        'config': json['config'] == null ? undefined : json['config'],
        'points': json['points'] == null ? undefined : json['points'],
    };
}

export function FlagToJSON(value?: Flag | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'uuid': value['uuid'],
        'style': value['style'],
        'config': value['config'],
        'points': value['points'],
    };
}

