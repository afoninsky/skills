package dev.example.account

import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable

@Composable
fun AccountScreen(onDelete: () -> Unit) {
    Button(onClick = onDelete) {
        Text("Delete account")
    }
}

