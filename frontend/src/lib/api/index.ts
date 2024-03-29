import { ClassFromJSON, type Class, type Lesson, LessonFromJSON } from './models/index';

/* tslint:disable */


/* eslint-disable */
export * from './runtime';
export * from './apis/index';
export * from './models/index';

const server_url = 'http://localhost:8080/api/v1';

export async function getClasses(): Promise<Class[]> {
    try {
        const response = await fetch(`${server_url}/class`);
        const data = await response.json();
        const classes = data.map((class_data: any) => ClassFromJSON(class_data));
        return classes;
    } catch (error) {
        console.error('Error:', error);
        return [];
    }
}

export async function getClassById(class_id: string): Promise<Class | null> {
    try {
        const response = await fetch(`${server_url}/class?id=${class_id}`);
        const data = await response.json();
        return ClassFromJSON(data[0]);
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

export async function createClass(class_data: Class): Promise<Class | null> {
    try {
        const response = await fetch(`${server_url}/class`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(class_data),
        });
        const data = await response.json();
        return ClassFromJSON(data);
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

export async function updateClass(class_id: string, class_data: Class): Promise<Class | null> {
    try {
        const response = await fetch(`${server_url}/class/${class_id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(class_data),
        });
        const data = await response.json();
        return ClassFromJSON(data);
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

export async function deleteClass(class_id: string): Promise<boolean> {
    try {
        const response = await fetch(`${server_url}/class/${class_id}`, {
            method: 'DELETE',
        });
        await response.json();
        return true;
    } catch (error) {
        console.error('Error:', error);
        return false;
    }
}

export async function getLessonsByClassId(class_id: string): Promise<Lesson[]> {
    try {
        const response = await fetch(`${server_url}/class/${class_id}/lesson`);
        const data = await response.json();
        const lessons = data.map((lesson_data: any) => LessonFromJSON(lesson_data));
        return lessons;
    } catch (error) {
        console.error('Error:', error);
        return [];
    }
}

export async function getLessonById(class_id: string, lesson_id: string): Promise<Lesson | null> {
    try {
        const response = await fetch(`${server_url}/class/${class_id}/lesson?id=${lesson_id}`);
        const data = await response.json();
        return LessonFromJSON(data[0]);
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

export async function createLesson(class_id: string, lesson_data: Lesson): Promise<Lesson | null> {
    try {
        const response = await fetch(`${server_url}/class/${class_id}/lesson`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(lesson_data),
        });
        const data = await response.json();
        return LessonFromJSON(data);
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

export async function updateLesson(class_id: string, lesson_id: string, lesson_data: Lesson): Promise<Lesson | null> {
    try {
        const response = await fetch(`${server_url}/class/${class_id}/lesson/${lesson_id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(lesson_data),
        });
        const data = await response.json();
        return LessonFromJSON(data);
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

export async function deleteLesson(class_id: string, lesson_id: string): Promise<boolean> {
    try {
        const response = await fetch(`${server_url}/class/${class_id}/lesson/${lesson_id}`, {
            method: 'DELETE',
        });
        await response.json();
        return true;
    } catch (error) {
        console.error('Error:', error);
        return false;
    }
}

export async function getAllFlags(class_id: string, lesson_id: string): Promise<any> {
    try {
        const response = await fetch(`${server_url}/class/${class_id}/lesson/${lesson_id}/flag`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
        return [];
    }
}
