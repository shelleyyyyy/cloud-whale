import PocketBase from 'pocketbase';
import { writable } from 'svelte/store';

export const pb = new PocketBase('http://10.4.3.62:8090'); 

export const currentUser = writable(pb.authStore.model);

pb.authStore.onChange((auth) => {
    console.log('authStore changed', auth);
    currentUser.set(pb.authStore.model);
});