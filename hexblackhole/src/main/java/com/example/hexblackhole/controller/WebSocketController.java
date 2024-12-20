package com.example.hexblackhole.controller;

import com.example.hexblackhole.dto.ChatMessageRequest;
import com.example.hexblackhole.dto.ChatMessageResponse;
import lombok.Getter;
import org.springframework.messaging.handler.annotation.DestinationVariable;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;

@RestController
public class WebSocketController {

    private final ConcurrentHashMap<Long, List<ChatMessageResponse>> chatHistory = new ConcurrentHashMap<>();

    @MessageMapping("/chat.{chatRoomId}")
    @SendTo("/subscribe/chat.{chatRoomId}")
    public ChatMessageResponse sendMessage(ChatMessageRequest request, @DestinationVariable Long chatRoomId) {
        List<ChatMessageResponse> messages = chatHistory.computeIfAbsent(chatRoomId, k -> new ArrayList<>());
        ChatMessageResponse response = new ChatMessageResponse(request.username(), request.content());
        messages.add(response);
        return response;
    }

    public List<ChatMessageResponse> getChatHistory(Long chatRoomId) {
        return chatHistory.getOrDefault(chatRoomId, Collections.emptyList());
    }
}
