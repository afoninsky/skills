package dev.example.account

import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import org.junit.Rule
import org.junit.Test

class AccountScreenTest {
    @get:Rule val compose = createComposeRule()

    @Test fun deleteButtonCanBePressed() {
        compose.setContent { AccountScreen {} }
        compose.onNodeWithText("Delete account").performClick()
    }
}

