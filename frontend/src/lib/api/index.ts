/* tslint:disable */

import { ClassFromJSON, type Class, type Lesson, LessonFromJSON } from './models/index';

/* eslint-disable */
export * from './runtime';
export * from './apis/index';
export * from './models/index';

const server_url = 'http://localhost:8000/api/v1'

export function getClasses(): Class[] {
    fetch(`${server_url}/class`).then(response => response.json()).then(data => {
        var classes = data.map((class_data: any) => ClassFromJSON(class_data))
        return classes
    }).catch(error => {
        console.error('Error:', error);
        return []
    });
    return [];
}

export function getClassById(class_id: string): Class | null {
    fetch(`${server_url}/class/${class_id}`).then(response => response.json()).then(data => {
        return ClassFromJSON(data)
    }).catch(error => {
        console.error('Error:', error);
        return null
    });
    return null;
}

export function createClass(class_data: Class): Class | null {
    fetch(`${server_url}/class`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(class_data),
    }).then(response => response.json()).then(data => {
        return ClassFromJSON(data)
    }).catch(error => {
        console.error('Error:', error);
        return null
    });
    return null;
}

export function updateClass(class_id: string, class_data: Class): Class | null {
    fetch(`${server_url}/class/${class_id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(class_data),
    }).then(response => response.json()).then(data => {
        return ClassFromJSON(data)
    }).catch(error => {
        console.error('Error:', error);
        return null
    });
    return null;
}

export function deleteClass(class_id: string): boolean {
    fetch(`${server_url}/class/${class_id}`, {
        method: 'DELETE',
    }).then(response => response.json()).then(data => {
        return true
    }).catch(error => {
        console.error('Error:', error);
        return false
    });
    return false;
}

export function getLessonsByClassId(class_id: string): Lesson[] {
    fetch(`${server_url}/class/${class_id}/lesson`).then(response => response.json()).then(data => {
        var lessons = data.map((lesson_data: any) => LessonFromJSON(lesson_data))
        return lessons
    }).catch(error => {
        console.error('Error:', error);
        return []
    });
    return [];
}
export function getLessonById(class_id: string, lesson_id: string): Lesson | null{
    fetch(`${server_url}/class/${class_id}/lesson/${lesson_id}`).then(response => response.json()).then(data => {
        return LessonFromJSON(data)
    }).catch(error => {
        console.error('Error:', error);
        return null
    });
    return null;
}
export function createLesson(class_id: string, lesson_data: Lesson): Lesson | null{
    fetch(`${server_url}/class/${class_id}/lesson`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(lesson_data),
    }).then(response => response.json()).then(data => {
        return LessonFromJSON(data)
    }).catch(error => {
        console.error('Error:', error);
        return null
    });
    return null;
}
export function updateLesson(class_id: string, lesson_id: string, lesson_data: Lesson): Lesson | null{
    fetch(`${server_url}/class/${class_id}/lesson/${lesson_id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(lesson_data),
    }).then(response => response.json()).then(data => {
        return LessonFromJSON(data)
    }).catch(error => {
        console.error('Error:', error);
        return null
    });
    return null;
}
export function deleteLesson(class_id: string, lesson_id: string): boolean{
    fetch(`${server_url}/class/${class_id}/lesson/${lesson_id}`, {
        method: 'DELETE',
    }).then(response => response.json()).then(data => {
        return true
    }).catch(error => {
        console.error('Error:', error);
        return false
    });
    return false;
}
