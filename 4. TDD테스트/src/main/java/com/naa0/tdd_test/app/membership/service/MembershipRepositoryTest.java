package com.naa0.tdd_test.app.membership.service;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;

import com.naa0.tdd_test.app.membership.repository.MembershipRepository;

public class MembershipRepositoryTest {
    @Autowired
    private MembershipRepository membershipRepository;

    @Test
    public void Repository가Null아님(){
        assertThat();
    }
}
